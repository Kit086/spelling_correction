# Define a variable for max_length
$max_length = 4096

# Check if the virtual environment exists
if (Test-Path .\Scripts) {
    Write-Host "The virtual environment already exists."
} else {
    # Create a virtual environment
    Write-Host "Creating a virtual environment..."
    py -m venv .
}

# Activate the python environment
Write-Host "Activating the python environment..."
.\Scripts\activate

# Update pip
Write-Host "Update pip..."
py -m pip install --upgrade pip

# Install the dependencies
Write-Host "Installing the dependencies..."
py -m pip install -r requirements.txt

# Run the main script with the max_length variable
Write-Host "Running the main script..."
py .\main.py $max_length

# Done
Write-Host "Done!"
