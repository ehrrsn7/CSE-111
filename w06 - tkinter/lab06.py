#!/usr/bin/env python3

SCREEN_HEIGHT   = 500
SCREEN_WIDTH    = 700

NAVY_BLUE = [
    "#152238",
    "#192841",
    "#1c2e4a",
    "#203354",
    "#23395d"
]

CLOUD_BLUE = "#223b4a"
CLOUD_BLUE_2 = "#2F5164"

GROUND_COLOR = "#230B1E"

STAR_COLORS = [
    "#dbe385",
    "#cbd480",
    "#bbc57b",
    "#abb676",
    "#9ba771",
    "#8b986c",
    "#7b8868",
    "#6c7963"
]

MOON_COLORS = [
    "#d6b354",
    "#d67754"
]

HOUSE_COLORS = [
    "#75674a",
    "#665940",
    "#594e38"
]

fps = 1
import time

import random

from tkinter import Tk, Canvas, Frame, BOTH

def main():
    root = Tk()
    frame = Frame()
    frame.master.title = "Tattooine"
    canvas = Canvas(frame)
    draw(frame, canvas)
    root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}+300+300")
    root.mainloop()


def draw(frame, canvas):

    # start drawing instructions
    frame.pack(fill=BOTH, expand=1)

    # draw background (blocky gradient)
    for i, blue in enumerate(NAVY_BLUE):
        canvas.create_rectangle(
            0, i * 100, 
            SCREEN_WIDTH, SCREEN_HEIGHT,
            fill=blue,
            outline=blue
        )

    # stars
    for i in range(random.randint(400, 600)):
        draw_star(canvas)

    # moons
    moon_radius = random.randint(150, 250)
    moon_x = random.randint(
        moon_radius, SCREEN_WIDTH - moon_radius)
    moon_y = random.randint(
        moon_radius, SCREEN_HEIGHT - moon_radius)

    canvas.create_oval(
        moon_x, moon_y,
        moon_x + moon_radius, moon_y + moon_radius,
        fill=MOON_COLORS[0],
        outline=MOON_COLORS[0]
    )

    moon_radius = random.randint(50, 150)
    moon_x = random.randint(moon_radius, SCREEN_WIDTH - moon_radius)
    moon_y = random.randint(moon_radius, SCREEN_HEIGHT - moon_radius)

    canvas.create_oval(
        moon_x, moon_y,
        moon_x + moon_radius, moon_y + moon_radius,
        fill=MOON_COLORS[1],
        outline=MOON_COLORS[1]
    )

    # generate clouds
    x = 0
    y = 100
    for i in range(0, SCREEN_WIDTH, 3):
        radius = random.randint(50, 100)
        canvas.create_oval(
            x, y, 10 + x + radius, y - radius,
            fill=CLOUD_BLUE,
            outline=CLOUD_BLUE
        )
        x += radius - 20
    
    x = 0
    y = 180
    for i in range(0, SCREEN_WIDTH, 3):
        radius = random.randint(50, 100)
        canvas.create_oval(
            x, y, 10 + x + radius, y - radius,
            fill=CLOUD_BLUE_2,
            outline=CLOUD_BLUE_2
        )
        x += radius - 20

    # house
    house_body_radius = 200
    house_position_left_x = random.randint(
        0, SCREEN_WIDTH - house_body_radius)

    canvas.create_rectangle(
        house_position_left_x - 20,
        SCREEN_WIDTH - (50 + 250),

        house_position_left_x + 10,
        SCREEN_WIDTH - 50,

        fill=HOUSE_COLORS[1],
        outline=HOUSE_COLORS[2],
        width="2p"
    )

    canvas.create_oval(
        house_position_left_x, 
        SCREEN_HEIGHT - 50 - house_body_radius/2,
        
        house_position_left_x + house_body_radius, 
        SCREEN_HEIGHT - 50 + house_body_radius/2,
        
        fill=HOUSE_COLORS[0],
        outline=HOUSE_COLORS[2],
        width="3p"
    )
    
    house_position_left_x += house_body_radius/4
    house_body_radius = 100

    canvas.create_rectangle(
        house_position_left_x - .25 * house_body_radius,
        SCREEN_HEIGHT - 50,
        
        house_position_left_x + 1.25 * house_body_radius,
        SCREEN_HEIGHT - 50 - house_body_radius/3,

        fill=HOUSE_COLORS[2],
        width="0"
    )
    
    canvas.create_oval(
        house_position_left_x, 
        SCREEN_HEIGHT - 50 - house_body_radius/2,
        
        house_position_left_x + house_body_radius, 
        SCREEN_HEIGHT - 50 + house_body_radius/2,
        
        fill=HOUSE_COLORS[0],
        outline=HOUSE_COLORS[2],
        width="3p"
    )
    
    house_position_left_x += house_body_radius/20
    house_body_radius = 90
    canvas.create_oval(
        house_position_left_x, 
        SCREEN_HEIGHT - 50 - house_body_radius/2,
        
        house_position_left_x + house_body_radius, 
        SCREEN_HEIGHT - 50 + house_body_radius/2,
        
        fill=HOUSE_COLORS[1],
        outline=HOUSE_COLORS[2],
        width="3p"
    )

    house_position_left_x += 250
    canvas.create_rectangle(
        house_position_left_x,
        SCREEN_HEIGHT - 50,

        house_position_left_x + 10,
        SCREEN_HEIGHT - 50 - 50,

        fill="black"
    )

    canvas.create_rectangle(
        house_position_left_x + 2,
        SCREEN_HEIGHT - 50,

        house_position_left_x + 8,
        SCREEN_HEIGHT - 50 - 80,

        fill="black"
    )

    canvas.create_rectangle(
        house_position_left_x + 4,
        SCREEN_HEIGHT - 50,

        house_position_left_x + 6,
        SCREEN_HEIGHT - 50 - 100,

        fill="black"
    )

    # ground
    canvas.create_rectangle(
        0, SCREEN_HEIGHT - 50,
        SCREEN_WIDTH, SCREEN_HEIGHT,
        fill="black"
    )

    # draw everything
    canvas.pack(fill=BOTH, expand=1)

def draw_star(canvas):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)

    avg_size = 4
    size_offset = 0.1 * random.randint(int(avg_size/2), int(avg_size*2))
    color = random.choice(STAR_COLORS)
        
    canvas.create_polygon(
        x + 1*size_offset, y,
        x, y - 5*size_offset,
        x, y + 5*size_offset,
        x + 1*size_offset, y,
        x - 1*size_offset, y,
        x, y - 5*size_offset,
        x, y + 5*size_offset,
        x - 1*size_offset, y,
        x, y,
        x, y + 1*size_offset,
        x - 4*size_offset, y,
        x, y - 1*size_offset,
        x, y + 1*size_offset,
        x + 4*size_offset, y,
        x, y - 1*size_offset,
        fill=color,
        outline=color
    )

if __name__ == "__main__":
    from os import system, name
    if name == "nt": _ = system("cls")
    else: _ = system("clear")
    main()