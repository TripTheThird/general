import tkinter as tk
import random




def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):

    canvas.create_oval(100, 100, 200, 200, fill="#ff0000")

    
    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom)
    draw_ground(canvas, scene_left, scene_top, scene_right, scene_bottom)
    draw_cloud(canvas, scene_left, scene_top, scene_right, scene_bottom)
    trees(canvas, scene_left, scene_top, scene_right, scene_bottom)
    draw_flower(canvas, scene_left, scene_top, scene_right, scene_bottom)
    draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)
   
# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    text_horizontal_margin = 20
    text_vertical_margin = 10

    for i in range (top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")

    for i in range (left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i + text_horizontal_margin, top + text_vertical_margin, text=f"{i}")
    
def draw_ground(canvas, left, top, right, bottom):
    canvas.create_rectangle(left, 300, right, bottom, fill="#90ee90")

def draw_sky(canvas, left, top, right, bottom):
    canvas.create_rectangle(left, top, right, bottom, fill="#87ceeb")

def draw_cloud(canvas, left, top, right, bottom):
    canvas.create_oval(150, 25, 275, 100, fill="white")
    canvas.create_oval(50, 50, 200, 150, fill="white")
    canvas.create_oval(150, 75, 300, 150, fill="white")
    canvas.create_oval (450, 75, 550, 150, fill="white")
    canvas.create_oval (550, 80, 670, 160, fill="white")
    canvas.create_oval (500, 15, 650, 150, fill="white")

#left #top #right #bottom
def draw_flower(canvas, left, top, right, bottom):
    numloop = 0

    while numloop <= 8:
        randomnumber = random.randrange(30, 770, 50)
        numloop = numloop + 1
        for i in range(left, right):
            canvas.create_line(randomnumber + 12, 275, randomnumber + 12, 300, fill="green")
            canvas.create_line(randomnumber + 11, 275, randomnumber + 11, 300, fill="green")
            canvas.create_line(randomnumber + 13, 275, randomnumber + 13, 300, fill="green")
            canvas.create_oval(randomnumber - 10, 253, randomnumber + 10, 272, fill="red")
            canvas.create_oval(randomnumber + 2, 250 - 10, randomnumber + 23, 275 - 10, fill="red")
            canvas.create_oval(randomnumber + 15, 253, randomnumber + 35, 272, fill="red")
            canvas.create_oval(randomnumber + 2, 250 + 10, randomnumber + 22, 275 + 10, fill="red")
            canvas.create_oval(randomnumber, 250, randomnumber + 25, 275, fill="yellow")

def trees(canvas, left, top, right, bottom):
    canvas.create_rectangle(400, 200, 420, 300, fill="brown")
    canvas.create_oval(375, 175, 445, 250, fill="green")

main()
