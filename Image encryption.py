import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import random

def encrypt_image(image_path, key, operation, value=None):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    width, height = img.size
    
    if operation == 'swap':
        pixels = swap_pixels(pixels, key)
    else:
        pixels = apply_operation(pixels, operation, value)
    
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(pixels)
    
    return encrypted_img

def decrypt_image(image_path, key, operation, value=None):
    img = Image.open(image_path)
    encrypted_pixels = list(img.getdata())
    width, height = img.size
    
    if operation == 'swap':
        encrypted_pixels = swap_pixels(encrypted_pixels, key, reverse=True)
    else:
        encrypted_pixels = apply_operation(encrypted_pixels, operation, value, reverse=True)
    
    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(encrypted_pixels)
    
    return decrypted_img

def swap_pixels(pixels, key, reverse=False):
    pixel_indices = list(range(len(pixels)))
    random.seed(key)
    random.shuffle(pixel_indices)
    
    if reverse:
        reverse_mapping = {pixel_indices[i]: i for i in range(len(pixel_indices))}
        swapped_pixels = [None] * len(pixels)
        for i in range(len(pixels)):
            swapped_pixels[reverse_mapping[i]] = pixels[i]
    else:
        swapped_pixels = [pixels[i] for i in pixel_indices]
    
    return swapped_pixels

def apply_operation(pixels, operation, value, reverse=False):
    if reverse:
        if operation == 'add':
            operation = 'subtract'
        elif operation == 'subtract':
            operation = 'add'
        elif operation == 'multiply':
            operation = 'divide'
        elif operation == 'divide':
            operation = 'multiply'
    
    new_pixels = []
    for pixel in pixels:
        if operation == 'add':
            new_pixel = tuple((p + value) % 256 for p in pixel)
        elif operation == 'subtract':
            new_pixel = tuple((p - value) % 256 for p in pixel)
        elif operation == 'multiply':
            new_pixel = tuple((p * value) % 256 for p in pixel)
        elif operation == 'divide':
            new_pixel = tuple((p // value) % 256 for p in pixel)
        new_pixels.append(new_pixel)
    
    return new_pixels

class ImageEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")

        self.image_path = ""

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=5)

        self.key_label = tk.Label(self.root, text="Key:")
        self.key_label.pack(pady=5)
        self.key_entry = tk.Entry(self.root)
        self.key_entry.pack(pady=5)

        self.operation_label = tk.Label(self.root, text="Operation:")
        self.operation_label.pack(pady=5)
        self.operation_var = tk.StringVar(self.root)
        self.operation_var.set("swap")
        self.operation_menu = tk.OptionMenu(self.root, self.operation_var, "swap", "add", "subtract", "multiply", "divide")
        self.operation_menu.pack(pady=5)

        self.value_label = tk.Label(self.root, text="Value (only for add, subtract, multiply, divide):")
        self.value_label.pack(pady=5)
        self.value_entry = tk.Entry(self.root)
        self.value_entry.pack(pady=5)

        self.encrypt_button = tk.Button(self.root, text="Encrypt Image", command=self.encrypt_image)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(self.root, text="Decrypt Image", command=self.decrypt_image)
        self.decrypt_button.pack(pady=5)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=5)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            img = Image.open(self.image_path)
            img.thumbnail((300, 300))
            self.img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.img_tk)
    
    def encrypt_image(self):
        key = self.key_entry.get()
        operation = self.operation_var.get()
        value = self.value_entry.get()
        value = int(value) if value else None

        if not self.image_path or not key:
            messagebox.showerror("Error", "Please load an image and enter a key.")
            return

        encrypted_img = encrypt_image(self.image_path, key, operation, value)
        encrypted_img_path = "encrypted_image.png"
        encrypted_img.save(encrypted_img_path)

        encrypted_img.thumbnail((300, 300))
        self.encrypted_img_tk = ImageTk.PhotoImage(encrypted_img)
        self.image_label.config(image=self.encrypted_img_tk)
        messagebox.showinfo("Success", f"Image encrypted and saved to {encrypted_img_path}")

    def decrypt_image(self):
        key = self.key_entry.get()
        operation = self.operation_var.get()
        value = self.value_entry.get()
        value = int(value) if value else None

        if not self.image_path or not key:
            messagebox.showerror("Error", "Please load an image and enter a key.")
            return

        decrypted_img = decrypt_image(self.image_path, key, operation, value)
        decrypted_img_path = "decrypted_image.png"
        decrypted_img.save(decrypted_img_path)

        decrypted_img.thumbnail((300, 300))
        self.decrypted_img_tk = ImageTk.PhotoImage(decrypted_img)
        self.image_label.config(image=self.decrypted_img_tk)
        messagebox.showinfo("Success", f"Image decrypted and saved to {decrypted_img_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptionApp(root)
    root.mainloop()
