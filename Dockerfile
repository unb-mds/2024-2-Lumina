# Imagem oficial do Python
FROM python:3.13-slim

# Definir o diretório de trabalho como /app
WORKDIR /app

# Variáveis de ambiente para o Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código fonte para o diretório de trabalho
COPY . .

# Expor a porta padrão do Django
EXPOSE 8000
