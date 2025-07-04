#ASSIGNMENT3


import tkinter as tk
def draw_rectangle(event):
    x,y=event.x , event.y
    canvas.create_rectangle(x-10,y-10,x+50,y+60 , width=10, outline="black",fill="blue")

def draw_oval(event):
    x,y=event.x , event.y
    canvas.create_oval(x-10,y-10,x+10,y+10 , outline="black",fill="orange")

def draw_arc(event):
    x,y=event.x , event.y
    canvas.create_arc(x-10,y-10,x+10,y+10 , outline="black",fill="green")
   
root=tk.Tk()   #create the main tk window
canvas=tk.Canvas(root,width=700,height=700)  #canvas:Create a canvas widget within the window
canvas.pack() #pack the canvas widget into the main window
canvas.bind("<Button-1>",draw_rectangle)
canvas.bind("<Button-2>",draw_oval)
canvas.bind("<Button-3>",draw_arc)
root.title("GUI suing Tkinter")
root.geometry("+1200+4000")   # set to coordinates 900,700
root.mainloop()