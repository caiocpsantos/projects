# Usar uma imagem base Node.js para o build
FROM node:18-alpine AS build

# Definir o diretório de trabalho
WORKDIR /app

# Copiar arquivos necessários
COPY package.json package-lock.json ./

# Instalar dependências
RUN npm install

# Copiar todo o código para o contêiner
COPY . .

# Fazer o build da aplicação
RUN npm run build

# Servir a aplicação com uma imagem leve de servidor web
FROM nginx:alpine

# Copiar os arquivos de build para o diretório padrão do Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Copiar configuração personalizada do Nginx (opcional)
# COPY nginx.conf /etc/nginx/nginx.conf

# Expor a porta 80
EXPOSE 80

# Comando para iniciar o servidor
CMD ["nginx", "-g", "daemon off;"]