# Use uma imagem oficial do Python como base
FROM python:3.9-slim

# Instalar netcat-openbsd ou netcat-traditional
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Definir variáveis de ambiente para evitar interações durante a instalação
ENV PYTHONUNBUFFERED 1

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de requisitos
COPY requirements.txt /app/

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto para o diretório de trabalho
COPY . /app/

# Tornar o script comash.sh executável
RUN chmod +x /app/comash.sh

# Comando para rodar o script de inicialização
CMD ["./comash.sh"]
