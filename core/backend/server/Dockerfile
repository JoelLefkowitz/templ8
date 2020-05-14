# Pull official python image
FROM python:latest

# Build dependencies first for imporved caching
COPY builder/ /{{ backend_name }}/builder/

WORKDIR /{ backend_name }}
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r builder/dependencies.txt

# Copy application
COPY . .

ENTRYPOINT ["bash", "builder/entrypoint.bash"]
