#! /bin/bash

echo -e "Start running the script!"

# Cambia al directorio 'website_frontend'
echo -e "Step 1: Changing directory to 'website_frontend'..."
cd website_frontend
# Crea un entorno virtual en el directorio actual llamado '.venv'
echo -e "Step 2: Creating a virtual environment named '.venv'..."
python -m venv .venv
# Activa el entorno virtual recién creado
echo -e "Step 3: Activating the virtual environment..."
source .venv/bin/activate
# Actualiza pip a la última versión dentro del entorno virtual
echo -e "Step 4: Upgrading pip to the latest version..."
pip install --upgrade pip
# Instala los paquetes Python requeridos especificados en requirements.txt en el entorno virtual
echo -e "Step 5: Installing required Python packages..."
pip install -r requirements.txt
# Elimina cualquier directorio existente llamado 'public'
echo -e "Step 5: Removing any existing 'public' directory..."
rm -rf public
# Inicializa reflex para el seguimiento de cambios
echo -e "Step 7: Initializing reflex for tracking changes..."
reflex init
# Exporta el frontend solo utilizando reflex con la API_URL especificada
echo -e "Step 8: Exporting frontend only using reflex with the specified API_URL..."
API_URL=https://api-dherreraj-dev.up.railway.app reflex export --frontend-only
# Descomprime el archivo 'frontend.zip' en el directorio 'public'
echo -e "Step 9: Unzipping 'frontend.zip' file into the 'public' directory..."
unzip frontend.zip -d public
# Elimina el archivo 'frontend.zip'
echo -e "Step 10: Removing 'frontend.zip' file..."
rm -f frontend.zip
# Desactiva el entorno virtual
echo -e "Step 11: Deactivating the virtual environment..."
deactivate

echo -e "All steps executed successfully."