FROM node:latest

# Build prod and dev dependencies before app to cache them
COPY package.json /{{webapp}}/package.json
WORKDIR /{{webapp}}
RUN npm i

COPY . /{{webapp}}/
ENV PATH /{{webapp}}/node_modules/.bin:$PATH
RUN ng build --output-path /etc/nginx/html/
COPY nginx.conf /etc/nginx
