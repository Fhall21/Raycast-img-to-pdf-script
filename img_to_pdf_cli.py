#!/usr/bin/env python3
"""
img_to_pdf_cli.py
Converts all images in a folder or a single image file to a PDF (headless, for Raycast script-commands).
Usage: python img_to_pdf_cli.py [image_folder_or_file] [output_pdf]
If no arguments are provided, uses GUI dialogs to select paths.
"""
import os
import sys

# Try import PIL and handle missing dependency with GUI message
try:
    from PIL import Image
except ImportError:
    try:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk(); root.withdraw()
        messagebox.showerror("Missing Dependency", "Pillow is required. Please install with:\npip install pillow")
    except:
        print("Pillow is required. Please install with: pip install pillow", file=sys.stderr)
    sys.exit(1)

# GUI dialogs
import tkinter as tk
from tkinter import filedialog, messagebox

def main():
    # Initialize tkinter root
    root = tk.Tk(); root.withdraw()

    # Get input path
    if len(sys.argv) >= 2:
        input_path = sys.argv[1]
    else:
        choice = messagebox.askquestion("Input Type", "Convert entire folder? (Yes) or single image file? (No)")
        if choice == 'yes':
            input_path = filedialog.askdirectory(title="Select Image Folder")
        else:
            input_path = filedialog.askopenfilename(
                title="Select Image File",
                filetypes=[
                    ("Image files", ("*.png", "*.jpg", "*.jpeg", "*.bmp", "*.gif", "*.tiff"))
                ]
            )
    if not input_path:
        sys.exit(1)

    # Get output path
    if len(sys.argv) >= 3:
        output = sys.argv[2]
    else:
        default_dir = os.path.dirname(input_path) if os.path.exists(input_path) else os.getcwd()
        output = filedialog.asksaveasfilename(title="Save PDF As",
            defaultextension=".pdf", filetypes=[("PDF files", '*.pdf')], initialdir=default_dir)
    if not output:
        sys.exit(1)

    # Determine files list
    if os.path.isfile(input_path):
        folder = os.path.dirname(input_path) or '.'
        image_files = [os.path.basename(input_path)]
    else:
        folder = input_path
        image_files = [f for f in os.listdir(folder) if f.lower().endswith((
            '.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff'))]
        image_files.sort()

    if not image_files:
        messagebox.showinfo("No Images", "No images found to convert.")
        sys.exit(1)

    # Load images
    images = []
    for file in image_files:
        try:
            img = Image.open(os.path.join(folder, file)).convert("RGB")
            images.append(img)
        except Exception as e:
            messagebox.showwarning("Load Error", f"Failed to load {file}: {e}")

    if not images:
        messagebox.showerror("Conversion Error", "No valid images to convert.")
        sys.exit(1)

    # Save PDF
    try:
        images[0].save(output, save_all=True, append_images=images[1:])
        messagebox.showinfo("Success", f"PDF saved successfully at {output}")
    except Exception as e:
        messagebox.showerror("Save Error", f"Failed to save PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
