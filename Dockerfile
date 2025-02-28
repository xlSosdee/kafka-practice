# Usa una imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Se define un ENTRYPOINT para ejecutar scripts dinámicamente
ENTRYPOINT ["python"]
