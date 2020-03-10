# Pull official python image
FROM python:latest

# Build dependencies first for imporved caching
COPY requirements.txt /{{server}}/requirements.txt

WORKDIR /{{server}}
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Gunicorn may not be in requierements.txt
RUN pip install gunicorn

# Copy application
COPY . .

ENTRYPOINT ["bash", "entrypoint.bash"]
