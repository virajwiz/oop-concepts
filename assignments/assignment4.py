import tkinter as tk

def draw_rectangle(event):
    x, y = event.x, event.y
    canvas.create_rectangle(x-10, y-10, x+50, y+60, width=2, outline="black", fill="blue")

def draw_triangle(event):
    x, y = event.x, event.y
    canvas.create_polygon(x, y-25, x-25, y+25, x+25, y+25, outline="black", fill="red")

root = tk.Tk()
root.title("Drawing Shapes")

canvas = tk.Canvas(root, width=800, height=500, bg="white")
canvas.pack()

button_rectangle = tk.Button(root, text="Draw Rectangle", command=lambda: canvas.bind("<Button-1>", draw_rectangle))
button_rectangle.pack()

button_triangle = tk.Button(root, text="Draw Triangle", command=lambda: canvas.bind("<Button-1>", draw_triangle))
button_triangle.pack()

root.mainloop()