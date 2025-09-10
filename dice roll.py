import tkinter as tk
import random
from PIL import Image, ImageTk
import os

# === Load dice images ===
def load_dice_images():
    dice_imgs = {}
    for i in range(1, 7):
        img_path = os.path.join("images", f"dice{i}.png")
        # Resize from 800x800 to 150x150 for GUI display
        img = Image.open(img_path).resize((150, 150), Image.Resampling.LANCZOS)
        dice_imgs[i] = ImageTk.PhotoImage(img)
    return dice_imgs

# === Roll the dice and update GUI ===
def roll_dice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)

    dice_label1.config(image=dice_images[d1])
    dice_label1.image = dice_images[d1]

    dice_label2.config(image=dice_images[d2])
    dice_label2.image = dice_images[d2]

    result_label.config(text=f"Total: {d1 + d2}")

# === GUI Setup ===
root = tk.Tk()
root.title("🎲 3D Dice Rolling Simulator")
root.geometry("800x800")
root.resizable(False, False)

# Load images
dice_images = load_dice_images()

# Dice labels
dice_label1 = tk.Label(root, image=dice_images[1])
dice_label1.pack(side="left", padx=20, pady=20)

dice_label2 = tk.Label(root, image=dice_images[1])
dice_label2.pack(side="right", padx=20, pady=20)

# Roll button
roll_button = tk.Button(root, text="Roll 🎲", command=roll_dice, font=("Helvetica", 14), bg="#007ACC", fg="white")
roll_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Click 'Roll' to start", font=("Helvetica", 14))
result_label.pack(pady=5)

# Start GUI loop
root.mainloop()
