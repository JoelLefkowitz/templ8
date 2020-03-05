# Multistage builds can't cache between stages
# Node modules install must therefore occur in its own Dockerfile
FROM node:latest AS builder

# Build prod and dev dependencies before app to cache them
COPY package.json /{{webapp}}/package.json
WORKDIR /{{webapp}}
RUN npm i
ENV PATH /{{webapp}}/node_modules/.bin:$PATH

COPY . /{{webapp}}/

# Example Angular build
RUN ng build

ONBUILD COPY --from=builder /{{webapp}}/dist/ /etc/nginx/html/
