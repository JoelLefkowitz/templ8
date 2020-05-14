FROM {{webapp}}_build:{{version}} as builder
FROM nginx:1.17.8
COPY --from=builder /etc/nginx/html/ /etc/nginx/html/
COPY --from=builder /etc/nginx/nginx.conf /etc/nginx/nginx.conf
