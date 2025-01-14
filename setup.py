from setuptools import setup, find_packages

setup(
    name="ollamaocr-python",  # Nome do pacote
    version="0.1.0",  # Versão inicial
    description="ollamaocr with Llama vision",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # Tipo do README
    author="Gabriel M. Cicotoste",
    author_email="gabrielmurilocicotoste6@gmail.com",
    url="https://github.com/Gao512/ollamaocr-python",  # Repositório do projeto
    packages=find_packages(),  # Encontra automaticamente subpacotes
    install_requires=[
        # Dependências do pacote
        "ollama",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Versão mínima do Python
)
