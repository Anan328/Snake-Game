try:
    import turtle
    import time
    import random
    from tkinter import *
    from tkinter.messagebox import *
    s=turtle.Screen()
    s.setup(600,600)
    s.cv._rootwindow.resizable(False,False)
    s.title("SnakeGame-Developed By ANAN")
    s.tracer(0)
    s.bgcolor("#465945")
    # turtle head
    head=turtle.Turtle()
    head.penup()
    head.direction="None"
    head.speed(0)
    head.shape("triangle")
    head.color("red")
    # write score
    score=0
    pen=turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(-285,275)
    pen.write("Score: "+str(score),font=("vijaya",20,"bold"))

    # write high_score
    high_score=0
    penh=turtle.Turtle()
    penh.hideturtle()
    penh.penup()
    penh.goto(150,275)
    penh.write("High Score: "+str(score),font=("vijaya",20,"bold"))

    # credit
    penc = turtle.Turtle()
    penc.color("#C02F1D")
    penc.hideturtle()
    penc.penup()
    penc.goto(145, -289)
    penc.write("©Developed By ANAN",font=("Courier New",10,"bold"))

    # food
    food=turtle.Turtle()
    food.penup()
    food.shape("circle")
    food.color("lime")
    food.speed(0)
    food.setpos(random.randint(-280,280), random.randint(-280, 270))

    segments=[]


    def up():
        if head.direction != "Down":
            head.direction = "Up"
            head.setheading(90)
    def down():
        if head.direction != "Up":
            head.direction = "Down"
            head.setheading(270)
    def left():
        if head.direction != "Right":
            head.direction = "Left"
            head.setheading(180)
    def right():
        if head.direction != "Left":
            head.direction = "Right"
            head.setheading(0)

    def move():
        x = head.xcor()
        y = head.ycor()
        if head.direction == "Up":
            head.sety(y+15)
        if head.direction == "Down":
            head.sety(y-15)
        if head.direction == "Left":
            head.setx(x-15)
        if head.direction == "Right":
            head.setx(x+15)
    turtle.listen()
    turtle.onkeypress(up,"Up")
    turtle.onkeypress(down,"Down")
    turtle.onkeypress(left,"Left")
    turtle.onkeypress(right,"Right")
    while True:
        try:
            s.update()
        except Exception:
            pass
        if head.ycor() > 280 or head.ycor() < -280 or head.xcor() > 280 or head.xcor() < -280 :
            pen.clear()
            score =0
            pen.write("Score: "+str(score),font=("vijaya",20,"bold"))
            win = Tk()
            win.withdraw()
            showwarning("You Lose!!", "Collision!")
            food.setpos(random.randint(-280, 280), random.randint(-280, 270))
            head.direction = "None"
            head.goto(0,0)
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
        for segment in segments:
            if segment.distance(head) < 15:
                pen.clear()
                score =0
                pen.write("Score: "+str(score),font=("vijaya",20,"bold"))
                win = Tk()
                win.withdraw()
                showwarning("You Lose!!", "Collision!")
                food.setpos(random.randint(-280, 280), random.randint(-280, 270))
                head.goto(0, 0)
                head.direction = "stop"

                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
                segments.clear()

        if head.distance(food)<20:
            pen.clear()
            penh.clear()
            score+=1
            if score>high_score:
                high_score=score
                penh.write("High Score: " + str(score), font=("vijaya", 20, "bold"))
            penh.write("High Score: " + str(high_score), font=("vijaya", 20, "bold"))
            pen.write("Score: "+str(score),font=("vijaya",20,"bold"))
            food.setpos(random.randint(-280, 280), random.randint(-280, 270))
            segment_new = turtle.Turtle()
            segment_new.color("#5C1424")
            segment_new.shape("square")
            segment_new.speed(0)
            segment_new.penup()
            segments.append(segment_new)
        for index in range(len(segments)-1,0,-1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x,y)
        if len(segments)>0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()
        time.sleep(0.1)

    turtle.mainloop()
    s.exitonclick()
except Exception :
    pass
