# Raycast Script Command: Image/Folder to PDF

This project provides a Raycast script command to convert all images in a folder or a single image file to a PDF using Python and Pillow. It supports both command-line and GUI (Tkinter) operation.

## Features
- **Raycast integration**: Add the script to Raycast and run it from anywhere.
- **Automatic Python environment**: The script creates a `venv` and installs dependencies automatically on first run.
- **Flexible input**: Works with either a folder of images or a single image file.
- **User-friendly GUI**: If no arguments are provided, a Tkinter GUI will prompt you to select the input and output paths.
- **Supported formats**: PNG, JPG, JPEG, BMP, GIF, TIFF.

## Usage
- Place the script command (`img-to-pdf.sh`) and Python script (`img_to_pdf_cli.py`) in your Raycast script-commands directory.
- Add the directory to Raycast via Preferences → Extensions → + → Add Script Directory.
- Run the "Images to PDF" command from Raycast.

### Modes
- **With arguments**: You can run the script with two arguments (image folder/file and output PDF path) for fully automated conversion (no GUI).
- **Without arguments**: If run from Raycast or terminal with no arguments, a GUI will prompt you to select the input folder/file and output PDF location interactively.

## Setup
1. Ensure Python 3 is installed on your system.
2. No need to manually install Pillow; the script will create a virtual environment and install dependencies automatically on first run.

## Example
Run via Raycast (recommended):
- Open Raycast and run "Images to PDF". Follow the GUI prompts.

Or via terminal:
```sh
./img-to-pdf.sh "/path/to/images" "/path/to/output.pdf"
```

## Notes
- The `venv/` directory is auto-created and excluded from git via `.gitignore`.
- The script works on macOS and requires Tkinter (included with most Python 3 installations).
- If Pillow is missing, a GUI error will prompt you to install it.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details

## Authors
- vibe coded by Felix Hall ([@fhall21](https://github.com/fhall21))
