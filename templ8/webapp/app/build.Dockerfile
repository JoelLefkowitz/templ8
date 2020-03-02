# Multistage builds can't cache between stages
# Node modules install must therefore occur in its own Dockerfile
FROM node:latest AS builder

# Build prod and dev dependencies before app to cache them
COPY package.json /{{name}}app/package.json
WORKDIR /{{name}}app
RUN npm i
ENV PATH /{{name}}app/node_modules/.bin:$PATH

COPY . /{{name}}app/

# Example Angular build
RUN ng build

ONBUILD COPY --from=builder /{{name}}app/dist/ /etc/nginx/html/
