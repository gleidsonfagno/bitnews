#!/bin/bash

echo "Iniciando o build_files.sh..."

# Criar ou ativar ambiente virtual
if [ ! -d "venv" ]; then
    python3.9 -m venv venv
fi
source venv/bin/activate

# Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

echo "build_files.sh concluído."
