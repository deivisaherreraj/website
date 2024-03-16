#! /bin/bash

echo -e "Start running the script!"
echo -e "Step 1: Upgrading pip..."
pip install --upgrade pip
echo -e "Step 2: Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt
echo -e "Step 3: Removing existing 'public' directory..."
rm -rf public
echo -e "Step 4: Initializing reflex..."
reflex init
echo -e "Step 5: Exporting with reflex (frontend-only)..."
reflex export --frontend-only
echo -e "Step 6: Unzipping frontend files to 'public' directory..."
unzip frontend.zip -d public
echo -e "Step 7: Removing frontend.zip..."
rm -f frontend.zip
echo -e "All steps executed successfully!"