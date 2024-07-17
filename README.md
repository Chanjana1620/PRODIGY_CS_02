# Image Encryption and Decryption Tool

This project is an interactive tool for encrypting and decrypting images using pixel manipulation techniques. It supports operations like swapping pixel values or applying basic mathematical operations to each pixel. The tool features a user-friendly graphical interface built with Tkinter.

## Features

- **Encryption and Decryption**: Securely encrypt and decrypt images based on a user-provided key.
- **Operations**: Perform pixel swapping or apply mathematical operations (add, subtract, multiply, divide).
- **Graphical User Interface**: Intuitive interface built with Tkinter.
- **File Handling**: Load, save, and display images within the application.

## Requirements

- Python 3.x
- Pillow
- Tkinter (usually included with Python installations)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/image-encryption-tool.git
    cd image-encryption-tool
    ```

2. Install the required packages:

    ```bash
    pip install Pillow
    ```

## Usage

1. Run the application:

    ```bash
    python image_encryption_gui.py
    ```

2. Use the GUI to:
    - Load an image
    - Enter an encryption key
    - Choose an operation (swap, add, subtract, multiply, divide)
    - Provide a value for the operation (if applicable)
    - Encrypt or decrypt the image
    - Save and display the results

## How It Works

### Encryption

- **Pixel Swapping**: Pixels are shuffled based on the provided key.
- **Mathematical Operations**: Basic arithmetic operations (addition, subtraction, multiplication, division) are applied to each pixel value.

### Decryption

- Uses the same key and operation to revert the image to its original state.

## Example

### Encrypt an Image Using Pixel Swapping

```bash
python image_encryption.py encrypt example.jpg encrypted_example.jpg my_secret_key swap
