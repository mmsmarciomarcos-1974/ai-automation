# 1. Imagem Base: Começamos com um Linux levinho que já tem Python instalado
FROM python:3.12-slim

# 2. Diretório de Trabalho: Criamos uma pasta dentro do container
WORKDIR /app

# 3. Cópia: Pegamos tudo da sua pasta atual e jogamos para dentro do container
COPY . .

# 4. Comando: Quando o container rodar, ele vai executar seus testes automaticamente
CMD ["python", "-m", "unittest", "discover", "tests"]