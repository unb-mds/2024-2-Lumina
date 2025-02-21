# Imagem oficial do Python
FROM python:3

# Definir o diretório de trabalho como /app
WORKDIR /app

# Variáveis de ambiente para o Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar as dependências
COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código fonte para o diretório de trabalho
COPY front/ ./
COPY src/ ./

# Expor a porta padrão do Django
EXPOSE 8000