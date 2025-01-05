#!/bin/bash
# Ativar ambiente virtual, se necessário
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Instalar pacotes necessários
pip install -r requirements.txt

# Coletar arquivos estáticos
python3.9 manage.py collectstatic --noinput
