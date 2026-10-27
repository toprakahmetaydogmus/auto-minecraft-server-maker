from setuptools import setup, find_packages

setup(
    name="auto-minecraft-server-maker",
    version="4.0.0",
    packages=find_packages(),
    py_modules=["main"],
    include_package_data=True,
    install_requires=[
        "customtkinter>=5.2.0",
        "requests>=2.28.0",
        "psutil>=5.9.0",
        "Pillow>=9.0.0",
        "darkdetect>=0.8.0",
    ],
    entry_points={
        "console_scripts": [
            "auto-minecraft-server-maker=main:main",
            "auto-mc=main:main",
        ],
    },
)
