	# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
#This function draws the top half of the scenery
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="skyblue3")

    center_x = 650
    bottom = 400    
    height = 450
    draw_cloud(canvas, center_x, bottom, height)
    center_x = 450
    bottom = 375    
    height = 455
    draw_cloud(canvas, center_x, bottom, height)
    center_x = 200
    bottom = 365    
    height = 480
    draw_cloud(canvas, center_x, bottom, height)
    draw_cloud(canvas, 50, 300, 400)
    draw_cloud(canvas, 20, 400, 450)
    draw_cloud(canvas, 700, 300, 500)



#This function draws a cloud.
def draw_cloud(canvas, center_x, bottom, height):
    cloud_width = height / 5
    cloud_height = height / 8
    cloud_left = center_x - cloud_width / 2
    cloud_right = center_x + cloud_width / 2
    cloud_top = bottom + cloud_height
    draw_oval(canvas, cloud_left, cloud_top, cloud_right, bottom, width=0, fill="lavender")
    fluff_width = height / 6
    fluff_height = height / 8
    fluff_left = center_x - fluff_width / 2
    fluff_right = center_x + fluff_width / 2
    fluff_top = bottom + fluff_height + 5
    fluff_bottom = bottom -5
    draw_arc(canvas, fluff_left, fluff_top, fluff_right - 20, bottom,  start=0, extent=180, width=0, outline="", fill="lavender")
    draw_arc(canvas, fluff_left + 20, fluff_top, fluff_right, bottom,  start=0, extent=180, width=0, outline="", fill="lavender")
    draw_arc(canvas, fluff_left + 25, fluff_top, fluff_right, fluff_bottom,  start=0, extent=-180, width=0, outline="", fill="lavender")

#This function shows the bottom half of the scenery.
def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="palegreen3")
    draw_rock(canvas, 508, 60, 168)
    draw_rock(canvas, 491, 60, 168)

    center_x = 150
    bottom = 100
    height = 190
    draw_tree(canvas, center_x, bottom, height)
    center_x = 25
    bottom = 95
    height = 173
    draw_tree(canvas, center_x, bottom, height)
    center_x = 15
    bottom = 80
    height = 170
    draw_tree(canvas, center_x, bottom, height)
    center_x = 50
    bottom = 50
    height = 175
    draw_tree(canvas, center_x, bottom, height)
    center_x = 60
    bottom = 45
    height = 185
    draw_tree(canvas, center_x, bottom, height)
    center_x = 75
    bottom = 40
    height = 185
    draw_tree(canvas, center_x, bottom, height)
    center_x = 95
    bottom = 33
    height = 170
    draw_tree(canvas, center_x, bottom, height)
    draw_tree(canvas, 300, 50, 250)
    draw_tree(canvas, 500, 60, 170)
    draw_rock(canvas, 489, 58, 167)
    draw_rock(canvas, 509, 58, 168)
    draw_rock(canvas, 492, 56, 168)
    draw_rock(canvas, 505, 56, 168)
    draw_rock(canvas, 495, 55, 168)
    draw_rock(canvas, 503, 55, 168)
    draw_rock(canvas, 499, 54, 168)#middle
    draw_rock(canvas, 478, 44, 168)
    draw_pond(canvas, 800, -10, 500)
    draw_rock(canvas, 750, 30, 600)





#This function draws a tree including the trunk and the top part.
def draw_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, width=1, fill="sienna4")
    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height
    draw_polygon(canvas, center_x, skirt_top, skirt_right, trunk_top, skirt_left, trunk_top, outline="forestgreen", width=1, fill="darkgreen")

#This function draws a small rock
def draw_rock(canvas,  center_x, bottom, height):
    rock_width = height / 16
    rock_height = height / 24
    rock_left = center_x - rock_width / 2
    rock_right = center_x + rock_width / 2
    rock_top = bottom + rock_height
    draw_oval(canvas, rock_left, rock_top, rock_right, bottom, outline="black", width=1, fill="grey")

def draw_pond(canvas, center_x, bottom, height):
    pond_width = height / 2
    pond_height = height / 4
    pond_left = center_x - pond_width / 2
    pond_right = center_x + pond_width / 2
    pond_top = bottom + pond_height

    draw_oval(canvas,pond_left, pond_top, pond_right, bottom, outline="sandybrown", width=4, fill="cornflowerblue" )

# Call the main function so that
# this program will start executing.
main()
