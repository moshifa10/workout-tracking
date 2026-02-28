import turtle

def draw_chiefs_flag():
    # Setup the screen
    screen = turtle.Screen()
    screen.title("Kansas City Chiefs Flag")
    screen.setup(width=800, height=600)
    
    t = turtle.Turtle()
    t.speed(3)
    
    # 1. Draw Red Background
    t.penup()
    t.goto(-300, 200)
    t.pendown()
    t.color("#E31837") # Chiefs Red
    t.begin_fill()
    for _ in range(2):
        t.forward(600)
        t.right(90)
        t.forward(400)
        t.right(90)
    t.end_fill()

    # 2. Draw White Arrowhead (Diamond)
    t.penup()
    t.goto(0, 150) # Top point
    t.pendown()
    t.color("black", "white")
    t.pensize(5)
    t.begin_fill()
    t.goto(200, 0)   # Right point
    t.goto(0, -150)  # Bottom point
    t.goto(-200, 0)  # Left point
    t.goto(0, 150)   # Back to top
    t.end_fill()

    # 3. Draw "KC" Text
    t.penup()
    t.goto(-10, -60)
    t.color("black")
    # Note: 'Arial Black' mimics the bold blocky style of the logo
    t.write("KC", align="center", font=("Arial Black", 80, "bold"))

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_chiefs_flag()