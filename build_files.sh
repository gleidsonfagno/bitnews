#!/bin/bash
echo "Iniciando o build_files.sh..."

# Instalar Pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py

echo "Pip instalado, verificando versão..."
pip --version

# Ativar ambiente virtual, se necessário
if [ -d "venv" ]; then
    echo "Ativando ambiente virtual..."
    source venv/bin/activate
fi

# Instalar pacotes necessários
echo "Instalando pacotes do requirements.txt..."
pip install -r requirements.txt

# Coletar arquivos estáticos
echo "Coletando arquivos estáticos..."
python3.9 manage.py collectstatic --noinput

echo "build_files.sh concluído."
