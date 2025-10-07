import tkinter as tk
from PIL import Image, ImageTk
import math, time, threading

# Window setup
root = tk.Tk()
root.title("J.A.R.V.I.S. Arc Reactor GUI")
root.geometry("600x600")
root.configure(bg='black')

# Load and display arc reactor background image
arc_image = Image.open("arc_reactor.png")  # Place your image in the same folder
arc_image = arc_image.resize((500, 500))
arc_photo = ImageTk.PhotoImage(arc_image)

canvas = tk.Canvas(root, width=600, height=600, bg='black', highlightthickness=0)
canvas.pack()
canvas.create_image(300, 300, image=arc_photo)

# Create pulsing center circle
def pulse():
    radius = 30
    growing = True
    while True:
        canvas.delete("pulse")
        canvas.create_oval(300 - radius, 300 - radius, 300 + radius, 300 + radius,
                           fill="cyan", outline="", tags="pulse")
        root.update()
        time.sleep(0.05)
        if growing:
            radius += 1
            if radius > 40:
                growing = False
        else:
            radius -= 1
            if radius < 30:
                growing = True

# Start pulsing animation in separate thread
threading.Thread(target=pulse, daemon=True).start()

# Display voice state
status_text = canvas.create_text(300, 550, text="[ J.A.R.V.I.S Ready ]", fill="cyan",
                                 font=("Orbitron", 20))

# Run loop
root.mainloop()
