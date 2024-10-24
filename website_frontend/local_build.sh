#! /bin/bash

echo -e "Start running the script!"

echo -e "Step 1: Activating the virtual environment..."
source .venv/bin/activate

echo -e "Step 2: Upgrading pip..."
pip install --upgrade pip

echo -e "Step 3: Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt

echo -e "Step 4: Removing existing 'public' directory..."
rm -rf public

echo -e "Step 5: Initializing reflex..."
reflex init

echo -e "Step 6: Exporting with reflex (frontend-only)..."
reflex export --frontend-only

echo -e "Step 7: Unzipping frontend files to 'public' directory..."
unzip frontend.zip -d public

echo -e "Step 8: Removing frontend.zip..."
rm -f frontend.zip

echo -e "All steps executed successfully!"