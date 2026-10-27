# -*- coding: utf-8 -*-
"""
AI Server Engineer & Autonomous Diagnostic Engine
Unified support for 12+ leading AI Providers:
1. NVIDIA NIM (api.nvcf.nvidia.com / integrate.api.nvidia.com)
2. OpenRouter (openrouter.ai)
3. OpenAI (ChatGPT / GPT-4o)
4. Anthropic (Claude 3.5 Sonnet)
5. Google Gemini (Gemini 1.5 Flash / Pro)
6. Groq (Ultra-fast Llama 3)
7. Mistral AI (Mistral Large / Codestral)
8. Together AI (Open source models)
9. Perplexity (Online search grounded AI)
10. Cohere (Command R+)
11. DeepSeek (DeepSeek V3 / R1)
12. Ollama / Local LLM (100% Free & Offline)
"""

import json
import urllib.request
import urllib.error
import logging

class AIEngineer:
    def __init__(self, config_manager=None):
        self.config_manager = config_manager

    def ask(self, prompt, system_prompt=None, provider_name=None, model=None, api_key=None, allow_fallback=True):
        """
        Unified query dispatcher across all 12 providers.
        If allow_fallback is True, automatically cascades to active providers upon failure.
        """
        if not system_prompt:
            system_prompt = (
                "Sen kıdemli bir Minecraft Sunucu Mühendisi ve Sistem Yöneticisisin. "
                "Sunucu kurulumu, arıza teşhisi, mod ve plugin uyumluluğu, performans optimizasyonu, "
                "Aikar JVM bayrakları, RCON ve komutlar konusunda uzmansın. "
                "Cevaplarını açık, adım adım, net ve Türkçe olarak ver."
            )

        ai_cfg = self.config_manager.get_ai_config() if self.config_manager else {}
        if not provider_name:
            provider_name = ai_cfg.get("active_provider", "Ollama (Yerel/Ücretsiz)")

        providers_dict = ai_cfg.get("providers", {})
        prov_info = providers_dict.get(provider_name, {})

        key = api_key if api_key is not None else prov_info.get("api_key", "")
        model_name = model if model else prov_info.get("default_model", "")
        base_url = prov_info.get("base_url", "")

        # Route by provider type
        if "Ollama" in provider_name:
            from core.local_ai_manager import LocalAIManager
            mgr = LocalAIManager()
            mgr.ensure_service_running()
            if not model_name or model_name == "llama3":
                local_models = mgr.list_local_models()
                if local_models:
                    model_name = local_models[0]
                else:
                    model_name = "qwen2.5:1.5b"

        # Primary call attempt
        result = self._dispatch_call(provider_name, prompt, system_prompt, model_name, key, base_url)

        # Autonomous Fallback Cascade: If failed and fallback enabled, try working alternatives
        if allow_fallback and ("Hatası" in result or "Bağlantı Hatası" in result or "Connection refused" in result):
            # 1. Try local Ollama if service is running
            try:
                from core.local_ai_manager import LocalAIManager
                lm = LocalAIManager()
                if provider_name != "Ollama (Yerel/Ücretsiz)" and lm.is_installed() and lm.ensure_service_running():
                    models = lm.list_local_models()
                    if models:
                        fallback_res = self._call_openai_compatible(
                            prompt, system_prompt, "http://127.0.0.1:11434/v1", models[0], "ollama", "Ollama (Yedek Yerel Motor)"
                        )
                        if not ("Hatası" in fallback_res or "Bağlantı Hatası" in fallback_res):
                            return f"[🛡️ Otonom AI Yedek Motoru (Ollama - {models[0]}) Devreye Girdi]:\n\n{fallback_res}"
            except Exception:
                pass

            # 2. Try any other provider that has an API key configured
            for alt_name, alt_info in providers_dict.items():
                if alt_name == provider_name or alt_name == "Ollama (Yerel/Ücretsiz)":
                    continue
                alt_key = alt_info.get("api_key", "")
                if alt_key and not alt_key.startswith("YOUR_"):
                    alt_res = self._dispatch_call(
                        alt_name, prompt, system_prompt, alt_info.get("default_model", ""), alt_key, alt_info.get("base_url", "")
                    )
                    if not ("Hatası" in alt_res or "Bağlantı Hatası" in alt_res):
                        return f"[🛡️ Otonom AI Yedek Motoru ({alt_name}) Devreye Girdi]:\n\n{alt_res}"

        return result

    def _dispatch_call(self, provider_name, prompt, system_prompt, model_name, key, base_url):
        if provider_name == "Google Gemini":
            return self._call_gemini(prompt, system_prompt, model_name, key)
        elif provider_name == "Anthropic":
            return self._call_anthropic(prompt, system_prompt, model_name, key)
        elif provider_name == "Cohere":
            return self._call_cohere(prompt, system_prompt, model_name, key)
        else:
            return self._call_openai_compatible(prompt, system_prompt, base_url, model_name, key, provider_name)

    def diagnose_installation_error(self, server_type, version, error_details):
        """Diagnoses installation/download failures and provides immediate actionable fix."""
        prompt = (
            f"Minecraft sunucusu indirilirken/kurulurken şu hata oluştu:\n"
            f"Sunucu Yazılımı: {server_type}, Minecraft Sürümü: {version}\n"
            f"Hata Ayrıntısı:\n```\n{error_details}\n```\n\n"
            f"Lütfen:\n"
            f"1. Bu hatanın neden kaynaklandığını (URL değişikliği, API kesintisi, Java sürümü vb.) açıkla.\n"
            f"2. Kullanıcının sunucuyu sorunsuz kurabilmesi için en hızlı alternatif çözümü (örn. hangi sürümü/yazılımı seçmeli veya hangi ayna linki kullanmalı) adım adım söyle."
        )
        return self.ask(prompt, allow_fallback=True)

    def analyze_log_error(self, log_snippet, provider_name=None):
        system_prompt = (
            "Sen uzman bir Minecraft Hata Ayıklama (Debug) Uzmanısın. "
            "Sana sunulan sunucu çökme raporunu veya hata logunu incele. "
            "1. Hatanın asıl kök sebebini (Hangi mod, plugin, Java sürümü veya eksik dosya) net olarak söyle. "
            "2. Sorunu çözmek için yapılacak kesin adım adım işlemi listele. "
            "3. Gerekiyorsa silinmesi veya güncellenmesi gereken mod/ayar dosyasını belirt."
        )
        prompt = f"Aşağıdaki Minecraft sunucu hatasını/çökmesini incele ve çözüm öner:\n\n```\n{log_snippet}\n```"
        return self.ask(prompt, system_prompt=system_prompt, provider_name=provider_name, allow_fallback=True)

    def optimize_server(self, player_count, ram_gb, server_type, mc_version):
        system_prompt = "Sen uzman bir Minecraft performans optimizasyonu mühendisisin."
        prompt = (
            f"Minecraft {mc_version} sürümünde {server_type} tipi bir sunucu kuruyorum. "
            f"Tahmini oyuncu sayısı: {player_count}, Ayrılan RAM: {ram_gb}GB. "
            f"En yüksek TPS ve sıfır lag elde etmek için en ideal server.properties, "
            f"varsa paper/purpur ayarlarını ve önerilen JVM başlatma parametrelerini ver."
        )
        return self.ask(prompt, system_prompt=system_prompt, allow_fallback=True)


    # -------------------------------------------------------------------------
    # Provider Implementations
    # -------------------------------------------------------------------------
    def _call_openai_compatible(self, prompt, system_prompt, base_url, model_name, api_key, provider_name):
        url = f"{base_url.rstrip('/')}/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        if provider_name == "OpenRouter":
            headers["HTTP-Referer"] = "https://github.com/toprakahmetaydogmus/auto-minecraft-server-maker"
            headers["X-Title"] = "Auto Minecraft Server Maker"

        payload = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.5
        }

        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            return f"[{provider_name} API Hatası {e.code}]: {err_body}"
        except Exception as e:
            if "Connection refused" in str(e) and "11434" in str(e):
                return "[Ollama Bağlantı Hatası]: Ollama servisiniz arka planda çalışmıyor olabilir. Lütfen 'ollama run llama3' komutunu çalıştırınız."
            return f"[{provider_name} Bağlantı Hatası]: {e}"

    def _call_gemini(self, prompt, system_prompt, model_name, api_key):
        if not api_key:
            return "[Gemini Hatası]: Google Gemini API anahtarı tanımlanmamış."
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [
                {"role": "user", "parts": [{"text": f"Sistem Talimatı: {system_prompt}\n\nKullanıcı: {prompt}"}]}
            ]
        }
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"[Gemini Hatası]: {e}"

    def _call_anthropic(self, prompt, system_prompt, model_name, api_key):
        if not api_key:
            return "[Anthropic Hatası]: Anthropic API anahtarı tanımlanmamış."
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01"
        }
        payload = {
            "model": model_name,
            "max_tokens": 1500,
            "system": system_prompt,
            "messages": [{"role": "user", "content": prompt}]
        }
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            return data["content"][0]["text"]
        except Exception as e:
            return f"[Anthropic Hatası]: {e}"

    def _call_cohere(self, prompt, system_prompt, model_name, api_key):
        if not api_key:
            return "[Cohere Hatası]: Cohere API anahtarı tanımlanmamış."
        url = "https://api.cohere.ai/v1/chat"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        payload = {
            "model": model_name,
            "preamble": system_prompt,
            "message": prompt
        }
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            return data.get("text", "")
        except Exception as e:
            return f"[Cohere Hatası]: {e}"
