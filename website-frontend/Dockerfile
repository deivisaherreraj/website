# Establece la imagen base como Python 3.11
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor como /app
WORKDIR /app

# Copia el contenido del directorio actual (del host) al directorio de trabajo en el contenedor
COPY . .

# Establece la variable de entorno VIRTUAL_ENV como /app/.venv_docker
ENV VIRTUAL_ENV=/app/.venv_docker

# Agrega el directorio de binarios del entorno virtual al PATH del sistema
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Crea un entorno virtual usando Python 3.11 en el directorio especificado
RUN python3.11 -m venv $VIRTUAL_ENV

# Actualiza pip a la última versión dentro del entorno virtual
RUN pip install --upgrade pip

# Instala los paquetes Python requeridos especificados en requirements.txt sin usar cache
RUN pip install --no-cache-dir -r requirements.txt

# Comando que se ejecutará al iniciar el contenedor
CMD reflex run --env prod --backend-only