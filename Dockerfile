# Etapa de compilação
FROM python:3.12-slim AS builder

# Configurando o ambiente de compilação
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /install

# Dependências nativas caso necessário para compilar alguma lib especifica
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Imagem de Produção Final
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Instalar libpq para o PostgreSQL runtime se precisasse (geralmente asyncpg não precisa do client c nativo, mas psycopg2-binary sim)
# Sendo puramente asyncpg, podemos ignorar. Mas é boa prática em containers C bindings.
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia as libs da fase de builder
COPY --from=builder /install /usr/local

# Copia o código da aplicação
COPY app /app/app
# Opcional: Arquivos raiz se existirem
COPY alembic.ini /app/
COPY README.md /app/

# Criar e configurar um usuário não root para maior segurança corporativa
RUN useradd -m -r -s /bin/bash appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
