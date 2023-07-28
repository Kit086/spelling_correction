#!/bin/bash

# Check if the virtual environment exists
if [ -d "./bin" ]; then
    echo "The virtual environment already exists."
else
    # Create a virtual environment
    echo "Creating a virtual environment..."
    python -m venv .
fi

# Activate the python environment
echo "Activating the python environment..."
source ./bin/activate

# Update pip
echo "Update pip..."
python -m pip install --upgrade pip

# Install the dependencies
echo "Installing the dependencies..."
python -m pip install -r requirements.txt

# Run the main script
echo "Running the main script..."
python ./main.py

# Done
echo "Done!"
