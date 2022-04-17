"""
SUTD 10.014 Computational Thinking for Design 2020 | 1D Project
F03 | Group 6
Sim Yu Hui, Kellie (1004204)
Wang Xilun (1004877)
M S Subesh Kumar (1005141)
Cheong Cher Lynn (1005458)
Muhammad Zulfiqar Bin Bakar (1005023)
"""

import random, time, turtle
t = turtle.Turtle(visible=False)
turtle.bgcolor("black")
ts = turtle.getscreen
turtle.screensize(canvwidth=1000, canvheight=600)
t.pencolor("white")

### cloning turtles and assigining to different functions
intro = t.clone()
d = t.clone()
a = t.clone()
b = t.clone()
c = t.clone()
border = t.clone()
bottom_border = t.clone()
name = t.clone()
h_bar = t.clone()
m_bar = t.clone()
s_bar = t.clone()
i_bar = t.clone()
finals = t.clone()
finals_content = t.clone()
finals_intro = t.clone()
exam_score_display = t.clone()
main = t.clone()
finale = t.clone()

### setting speed of turtle
d.speed(0)
a.speed(0)
b.speed(0)
c.speed(0)
border.speed(0)
bottom_border.speed(0)
name.speed(0)
h_bar.speed(0)
m_bar.speed(0)
s_bar.speed(0)
i_bar.speed(0)
finals.speed(0)
finals_content.speed(0)
finals_intro.speed(0)
exam_score_display.speed(0)
main.speed(0)
finale.speed(0)

### setting colours of the bars
h_bar.fillcolor('red')
m_bar.fillcolor('green')
s_bar.fillcolor('pink')
i_bar.fillcolor('blue')

### assigns attribute values based on character (randomly generated)
def assign_values(default_attributes, character):
    if (character % 2) == 1:
        value = 25
    else:
        value = -25

    if character == 1 or character == 2:
        default_attributes["health"] += value
    elif character == 3 or character == 4:
        default_attributes["money"] += value
    elif character == 5 or character == 6:
        default_attributes["social"] += value
    elif character == 7 or character == 8:
        default_attributes["intelligence"] += value

    intro.penup()
    intro.setposition(-40,30)
    intro_text = """Welcome to our Python game! 

In this game, you are an SUTD Freshmore student going through Term 1. 
You have a set number of points for each of the 4 attributes: 
Health, Money, Social, Intelligence.  

The values of the points are based on the character that you have been assigned.
These values are represented by the 4 different gauges you see here on your right.

You will be presented with a series of scenarios and the timeline alongside 
the points awarded will vary according to the choices you make. 

Do note that throughout the game, only lower case letters will be accepted.

Choose wisely and best of luck!"""
    intro.write(intro_text, font=('Arial','12','normal'), align=("center"))

### fill bars
def bar_fill(bar, value):
    bar.begin_fill()
    for i in range(4):
        if (i % 2 == 0):
            bar.forward(25)
            bar.left(90)
        else:
            bar.forward(value)
            bar.left(90)
    bar.end_fill()

### initial setting up of bars at start of game
def bar_initial_setup(attributes, char_name): 
    h_value = attributes[0]
    m_value = attributes[1]
    s_value = attributes[2]
    i_value = attributes[3]
    d.penup()
    a.penup()
    b.penup() 
    c.penup()
    d.setposition(300,300)
    a.setposition(350,300)
    b.setposition(400,300)
    c.setposition(450,300)

    for i in range(4):
        d.pendown()
        a.pendown()
        b.pendown()
        c.pendown()
        if (i % 2 == 0):
            d.forward(25)
            a.forward(25)
            b.forward(25)
            c.forward(25)
            d.right(90)
            a.right(90)
            b.right(90)
            c.right(90)
        else:
            d.forward(100)
            a.forward(100)
            b.forward(100)
            c.forward(100)
            d.right(90)
            a.right(90)
            b.right(90)
            c.right(90)

    d.penup()
    a.penup()
    b.penup() 
    c.penup()
    name.penup()
    d.setposition(310,300)
    a.setposition(360,300)
    b.setposition(410,300)
    c.setposition(460,300)
    name.setposition(350,180)
    d.pendown()
    a.pendown()
    b.pendown()
    c.pendown()
    name.pendown()
    d.write("H", font=('Arial','8','normal'))
    a.write("M", font=('Arial','8','normal'))
    b.write("S", font=('Arial','8','normal'))
    c.write("I", font=('Arial','8','normal'))
    name.write(char_name, font=('Arial','10','normal'), align=("left"))

    border.penup()
    border.setposition(280,320)
    border.pensize(5)
    for i in range(4):
        border.pendown()
        if (i % 2 == 0):
            border.forward(215)
            border.right(90)
        else:
            border.forward(150)
            border.right(90)

    h_bar.penup()
    m_bar.penup()
    s_bar.penup() 
    i_bar.penup()
    h_bar.setposition(300,200)
    m_bar.setposition(350,200)
    s_bar.setposition(400,200)
    i_bar.setposition(450,200)

    bar_fill(h_bar, h_value)
    bar_fill(m_bar, m_value)
    bar_fill(s_bar, s_value)    
    bar_fill(i_bar, i_value)

    bottom_border.penup()
    bottom_border.setposition(-650,-100)
    bottom_border.pendown()
    bottom_border.pensize(5)
    bottom_border.forward(1300)
    bottom_border.penup()
    bottom_border.setposition(-50,-125)
    bottom_border.pendown()
    bottom_border.write("Recent Activity", font=('Arial','12','bold'), align=('left'))

### update values to fill bars with 
def bar_update(attributes):
    h_value = attributes[0]
    m_value = attributes[1]
    s_value = attributes[2]
    i_value = attributes[3]
    h_bar.undo()
    m_bar.undo()
    s_bar.undo() 
    i_bar.undo()

    ### setting 0 as the minimum value for each attribute
    if h_value < 0:
        h_value = 0
        default_attributes["health"] = 0
    if m_value < 0:
        m_value = 0
        default_attributes["money"] = 0
    if s_value < 0:
        s_value = 0
        default_attributes["social"] = 0
    if i_value < 0:
        i_value = 0
        default_attributes["intelligence"] = 0

    ### setting 100 as the maximum value for each attribute
    if h_value > 100:
        h_value = 100
        default_attributes["health"] = 100
    if m_value > 100:
        m_value = 100
        default_attributes["money"] = 100
    if s_value > 100:
        s_value = 100
        default_attributes["social"] = 100
    if i_value > 100:
        i_value = 100
        default_attributes["intelligence"] = 100

    bar_fill(h_bar, h_value)
    bar_fill(m_bar, m_value)
    bar_fill(s_bar, s_value)    
    bar_fill(i_bar, i_value)

### get values of attributes
def get_attribute_value():
    h_value = default_attributes["health"]
    m_value = default_attributes["money"]
    s_value = default_attributes["social"]
    i_value = default_attributes["intelligence"]

    return (h_value, m_value, s_value, i_value)

### mini game to guess number
def guess_num_game():
    lower_guess = 0
    upper_guess = 40
    target = random.randint(lower_guess+1,upper_guess-1)

    #list of turtles and penup actions
    i = t.clone()
    ac = t.clone()
    m1 = t.clone()
    gn = t.clone()
    i.penup()
    ac.penup()
    m1.penup()
    gn.penup()

    instructions = """You have chosen to study alone, but is it really the best decision?\n
Beat the game to prove that you've got what it takes to go solo in your academic journey.\n
You have a total of 5 tries. Good luck!"""
    i.setposition(0,200)
    i.write(instructions, font=('Arial', '10', 'normal'), align='center')
    guess_num_score = 0

    for n in range(5):
        x_mvmt = 500*(n%2)
        y_mvmt = 80*(n//2)
        attempt_count = "Attempt " + str(n+1)
        x = -400+x_mvmt
        y = 160-y_mvmt
        ac.setposition(x,y)
        ac.write(attempt_count, font=('Arial','10','normal','bold','underline'), align='left')
        message1 = "Enter an integer between " + str(lower_guess) + " and " + str(upper_guess) + ": "
        y = 140-y_mvmt
        m1.setposition(x,y)
        m1.write(message1, font=('Arial','10','normal','bold'), align='left')
        title = "Guess the Number"
        string = turtle.textinput(title, message1)
        while len(string) == 0:
            string = turtle.textinput(title, message1)
        integer_test = True
        for index in range (0, len(string)):
            element = string[index:index+1]
            y = 90-y_mvmt
            gn.setposition(x,y)
            if ord(element) < 48 or ord(element) > 57:
                integer_test = False
                error_message = "You did not enter an integer.\n"
                if n < 3:
                    no_of_tries = "Try again, this time with an integer. You have " + str(4-n) + " tries left.\n"
                elif n == 3: 
                    no_of_tries = "This is your final guess. USE AN INTEGER!\n"
                else:
                    no_of_tries = "That was incorrect and you have exhausted your tries. Game over.\nAnd you thought studying alone would work out well?"
                emnot = error_message + no_of_tries
                gn.write(emnot, font=('Arial','10','normal','italic'), align='left')
        
        if integer_test == True:
            guess = int(string)
            if n < 3:
                no_of_tries = "You have " + str(4-n) + " tries left.\n"
            elif n == 3: 
                no_of_tries = "This is your final guess.\n"

            if n == 4:
                if guess < target or guess > target:
                    game_over = "That was incorrect and you have exhausted your tries. Game over.\nAnd you thought studying alone would work out well?"
                    gn.write(game_over, font=('Arial','10','normal','italic'), align='left')
                    break
                else:
                    number_reveal = str(target) + " is the right number.\n"
                    congrats = "Congratulations, I guess you'll really do just fine studying alone!\n"
                    gmnot = number_reveal + congrats
                    gn.write(gmnot, font=('Arial','10','normal','italic'), align='left')
                    break
                
            elif guess < lower_guess or guess > upper_guess:
                gauge_message = "Input is out of range. Look at the range and try again!\n"
                gmnot = gauge_message + no_of_tries
                gn.write(gmnot, font=('Arial','10','normal','italic'), align='left')
                
            elif guess > target:
                upper_guess = guess
                gauge_message = "Too high, go lower!\n"
                gmnot = gauge_message + no_of_tries
                gn.write(gmnot, font=('Arial','10','normal','italic'), align='left')

            elif guess < target:
                lower_guess = guess
                gauge_message = "Too low, go higher!\n"
                gmnot = gauge_message + no_of_tries
                gn.write(gmnot, font=('Arial','10','normal','italic'), align='left')
                
            else:
                number_reveal = str(target) + " is the right number.\n"
                congrats = "Congratulations, I guess you'll really do just fine studying alone!\n"
                gmnot = number_reveal + congrats
                gn.write(gmnot, font=('Arial','10','normal','italic'), align='left')
                break

    if guess == target:
        guess_num_score += 1   
        
    leave = turtle.textinput("Exit minigame?", "Enter 'yes' to exit")
    while leave != "yes":
        leave = turtle.textinput("Exit minigame?", "Enter 'yes' to exit")

    i.clear()
    ac.clear()
    m1.clear()
    gn.clear()

    return guess_num_score

## start hangman game
def hangman_game(char_name):
    hangman_score = 0
    pen = t.clone()
    pen2 = t.clone()
    text = t.clone()
    text2 = t.clone()
    text3 = t.clone()
    text4 = t.clone()
    text5 = t.clone()
    text6 = t.clone()
    turtle.colormode(255)

    #hide turtle
    pen.hideturtle()
    pen2.hideturtle()
    text.hideturtle()
    text2.hideturtle()
    text3.hideturtle()
    text4.hideturtle()
    text5.hideturtle()
    text6.hideturtle()

    pen.penup()
    pen2.penup()
    text.penup()
    text2.penup()
    text3.penup()
    text4.penup()
    text5.penup()
    text6.penup()

    pen.setposition(-100,-80)
    pen2.setposition(-97,-77)
    
    text.setposition(-90,280)
    text2.setposition(-200,100)
    text3.setposition(-250,-500)
    text4.setposition(80,70)
    text5.setposition(80,40)
    text6.setposition(100,0)

    pen.pendown()
    pen.speed(0)
    pen.pensize(6)
    pen2.pendown()
    pen2.speed(0)
    pen2.color(252,175,23)
    text.speed(0)
    text2.speed(0)

    #begin the game 
    hello_name = 'Hello ' + char_name + '!\n'
    context1 = """Welcome to the drinking game.
You have 8 tries to guess this word.
With every wrong guess, the amount of
beer increases! 
To get the correct answer, you need to 
unscramble all 5 letters.
If you fail to enter the correct answer
at the end, you will drink everything... 
and get wasted (:"""
    context2 = ""
    text.write(hello_name, font=('Arial', '20', 'normal'))
    time.sleep(1)
    text2.write(context1, font=('Arial','15','normal'))
    time.sleep(1)
    word = "study"
    guesses = ''
    turns = 8
    lst = []

    #bottle
    pen.left(90)
    pen.forward(150)
    pen.left(180)
    pen.forward(150)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(150)
    pen.left(180)
    pen.forward(50)
    pen.left(90)
    pen.forward(40)
    pen.right(90)
    pen.forward(70)
    pen.right(90)
    pen.forward(40)
    text.pendown()
    while turns > 0:
        time.sleep(1)
        text3.undo()
        text3.setposition(-600,0)
        text3.write(turns,font=('Arial','30','normal'))
        guess = turtle.textinput("Guess","What is your guess? (Only one letter)")
        if len(guess) == 1:
            if guess in word:
                if guess not in lst:
                    lst.append(guess)
                    text4.write(guess,font=('Arial', '20', 'normal'))
                    text4.forward(20)
                    turns -= 1
                elif guess in lst:
                    text5.write("There are no repeated letters in this word",font=('Arial','15','normal'))
                    time.sleep(1)
                    text5.undo()
            
            elif guess not in word:
                turns -= 1
                text5.write("Wrong",font=('Arial', '15', 'normal'))
                time.sleep(1)
                text5.undo()
                for i in range(10):
                    pen2.forward(93)
                    pen2.right(-90)
                    pen2.forward(1)
                    pen2.right(-90)
                    pen2.forward(93)
                    pen2.left(-90)
                    pen2.forward(1)
                    pen2.left(-90)

            if turns == 0 or sorted(lst) == sorted(list(word)):
                context3 = "\nIt's time to guess the word!"
                time.sleep(1)
                text3.forward(40)
                text3.write(context3,font=('Arial','25','normal'))
                time.sleep(1)
                answer = turtle.textinput("Question","What is the answer?")
                if answer == word:
                    text6.write("You won!",font=('Arial', '30', 'normal'))
                    hangman_score += 1
                    for i in range(900):
                        pen2.undo()
                    break
                elif answer != word:
                    text6.write("Wrong guess. Drink!!", font=('Arial', '30', 'normal'))
                    for i in range(900):
                        pen2.undo()
                    break
        else:
            turns -= 1
            text5.write("Please enter 1 letter.", font=('Arial', '15', 'normal'))
            time.sleep(1)
            text5.undo()
        text3.undo()

    proceed = turtle.textinput("Proceed", "Enter 'yes' to continue")
    while True:
        if proceed == 'yes':
            text.clear()
            text2.clear()
            text3.clear()
            text4.clear()
            text5.clear()
            text6.clear()
            for i in range(900):
                pen2.undo()
            for i in range(16):
                pen.undo()
            break
        else:
            proceed = turtle.textinput("Proceed", "Enter 'yes' to continue")

    return hangman_score

### draw exam paper for finals mini game
def draw_exam_paper():
    finals.penup()
    finals.setpos(-250, -85)
    finals.pendown()
    for i in range(4):
        if (i % 2 == 0):
            finals.forward(480)
            finals.left(90)
        else:
            finals.forward(425)
            finals.left(90)
    
    finals_intro.penup()
    finals_intro.setpos(-425, -55)
    message = """Finals is here!
Well this is it, everything you've learnt 
in this past term all comes down to this...
Try your best to get all 3 questions right (:
Break a leg!"""
    finals_intro.write(message, font=('Arial','12','bold'), align=('center'))

    finals.penup()
    finals.setpos(0, 315)
    finals.write("SUTD", font=('Arial','12','bold'), align=('center'))
    finals.setpos(0, 300)
    finals.write("Freshmore", font=('Arial','12','bold'), align=('center'))
    finals.setpos(0, 285)
    finals.write("Term 1", font=('Arial','12','bold'), align=('center'))

    finals_score = 0

    ### Start of Math Question ###
    finals_content.penup()
    finals_content.setpos(0,270)
    moduleName = "Modelling and Analysis"
    finals_content.write(moduleName, font=('Arial','12','bold'), align=('center'))

    finals.setpos(-250, 255)
    finals.pendown()
    finals.forward(480)
    finals.penup()

    finals_content.setpos(-240, 230)
    question = "Question 1"
    finals_content.write(question, font=('Arial','12','bold'), align=('left'))

    finals_content.setpos(-240,140)
    riddle = """I am a 2-digit odd number.  
I have 3 tens. 
My ones digit is the same as my tens digit. 
What am I?"""
    finals_content.write(riddle, font=('Arial','12','normal'), align=('left'))

    finals_content.setpos(-240, 60)
    riddleOption = ""
    finals_content.write(riddleOption, font=('Arial','12','normal'), align=('left'))   
    finals_content.setpos(-240, 20)
    finals_content.write("Ans: ________" , font=('Arial','12','normal'), align=('left'))
    answer = turtle.textinput(moduleName, "Enter Your Answer Here: ")
    if answer == '33':
        finals_score += 1
    for i in range(9):
        finals_content.undo()
    finals_intro.undo()
    ### End of Math Question ###

    ### Start of Physics Question ###
    finals_content.setpos(0,270)
    moduleName = "Physical World"
    finals_content.write(moduleName, font=('Arial','12','bold'), align=('center'))

    finals.setpos(-250, 255)
    finals.pendown()
    finals.forward(480)
    finals.penup()

    finals_content.setpos(-240, 230)
    question = "Question 2"
    finals_content.write(question, font=('Arial','12','bold'), align=('left'))

    finals_content.setpos(-240, 140)
    riddle = """There are 2 different buckets of water. 
Bucket A is at 25°C while Bucket B is at 25°F. 
If we drop a coin into each bucket, which one will hit the bottom first?"""
    finals_content.write(riddle, font=('Arial','12','normal'), align=('left'))

    finals_content.setpos(-240, 40)
    riddleOption = """a. Coin in A. 1 state is not like the other  
b. Coin in B. Water contracts more so there is less water resistance
c. Coin in A. it is at a higher temperature and has higher velocity
d. Y'all tryna trick me, it's the same
e. The mitochondria is the powerhouse of the cell"""
    finals_content.write(riddleOption, font=('Arial','12','normal'), align=('left'))   
    finals_content.setpos(-240, 0)
    finals_content.write("Ans: ________" , font=('Arial','12','normal'), align=('left'))
    answer = turtle.textinput(moduleName, "Enter Your Answer Here: ")
    if answer == 'a':
        finals_score += 1
    for i in range(9):
        finals_content.undo()
    ### End of Physics Question ###

    ### Start of CDT Question ###
    finals_content.setpos(0,270)
    moduleName = "Computational Thinking for Design"
    finals_content.write(moduleName, font=('Arial','12','bold'), align=('center'))

    finals.setpos(-250, 255)
    finals.pendown()
    finals.forward(480)
    finals.penup()

    finals_content.setpos(-240, 230)
    question = "Question 3"
    finals_content.write(question, font=('Arial','12','bold'), align=('left'))

    finals_content.setpos(-240, 190)
    riddle = "What is the subject code of Computational Thinking for Design?"
    finals_content.write(riddle, font=('Arial','12','normal'), align=('left'))

    finals_content.setpos(-240, 60)
    riddleOption = """a. 10.013
b. 10.014
c. 10.015 
d. 02.003
e. 01.018
f: 01.011
g: 01.009"""
    finals_content.write(riddleOption, font=('Arial','12','normal'), align=('left'))   
    finals_content.setpos(-240, 20)
    finals_content.write("Ans: ________" , font=('Arial','12','normal'), align=('left'))
    answer = turtle.textinput(moduleName, "Enter Your Answer Here: ")
    if answer == 'b':
        finals_score += 1
    for i in range(9):
        finals_content.undo()
    ### End of CDT Question ###

    for i in range(20):
        finals.undo()
    
    return finals_score

### display final attribute values
def display_finale(attributes):
        h_value = attributes[0]
        m_value = attributes[1]
        s_value = attributes[2]
        i_value = attributes[3]
        finale.penup()
        finale.setpos(0,300)
        finale.write("SUTD", font=('Arial','15','bold'), align=('center'))
        finale.setpos(0,270)
        finale.write("Freshmore", font=('Arial','15','bold'), align=('center'))
        finale.setpos(0,240)
        finale.write(char_name, font=('Arial','15','bold'), align=('center'))
        finale.setpos(0,210)
        finale.write("Final Statistics", font=('Arial','15','bold'), align=('center'))
        finale.setpos(0,150)
        h_str = "Health: " + str(h_value) + " points"
        finale.write(h_str, font=('Arial','18','bold'), align=('center'))
        finale.setpos(0,110)
        m_str = "Money: " + str(m_value) + " points"
        finale.write(m_str, font=('Arial','18','bold'), align=('center'))
        finale.setpos(0,70)
        s_str = "Social: " + str(s_value) + " points"
        finale.write(s_str, font=('Arial','18','bold'), align=('center'))
        finale.setpos(0,30)
        i_str = "Intelligence: " + str(i_value) + " points"
        finale.write(i_str, font=('Arial','18','bold'), align=('center'))

### credits scene
def thank_you():
        finale.setpos(0,300)
        finale.write("SUTD", font=('Arial','15','bold'), align=('center'))
        finale.setpos(0,270)
        finale.write("F03", font=('Arial','15','bold'), align=('center'))
        finale.setpos(0,240)
        finale.write("Group 6", font=('Arial','15','bold'), align=('center'))
        finale.setpos(0,210)
        finale.write("CTD 1D Project", font=('Arial','15','bold'), align=('center'))

        finale.setpos(0,150)
        finale.write("Cher Lynn", font=('Arial','18','bold'), align=('center'))
        finale.setpos(0,110)
        finale.write("Kellie", font=('Arial','18','bold'), align=('center'))
        finale.setpos(0,70)
        finale.write("Subesh", font=('Arial','18','bold'), align=('center'))
        finale.setpos(0,30)
        finale.write("Xilun", font=('Arial','18','bold'), align=('center'))
        finale.setpos(0,-10)
        finale.write("Zulfiqar", font=('Arial','18','bold'), align=('center'))
        finale.setpos(0,-70)
        finale.write("The end.", font=('Arial','15','bold'), align=('center'))
        finale.setpos(425,30)
        finale.write("Thank you for playing our game!", font=('Arial','15','bold'), align=('center'))
        finale.setpos(425,-20)
        finale.write("Please close the window to exit", font=('Arial','15','bold'), align=('center')) 

### check if any attributes have dipped to 0
def check_attributes(default_attributes):
    ### list of turtles and penup actions
    h0 = t.clone()
    m0 = t.clone()
    s0 = t.clone()
    i0 = t.clone()
    h0.penup()
    m0.penup()
    s0.penup()
    i0.penup()
    
    if default_attributes["health"] == 0:
        h0m1 = """You have neglected your health and are now gravely sick in the hospital. But money can cure anything, right?
Let's find out if your finances are sufficient to save you."""
        h0.setposition(0,110)
        h0.write(h0m1, font=('Arial','12','normal'), align='center')
        time.sleep(6)
        h0.setposition(0,75)
        h0.write("Calculating finances...", font=('Arial','11','normal'), align='center')
        time.sleep(2)
        if default_attributes["money"] >= 50:
            default_attributes["health"] = 25
            default_attributes["money"] -= 30
            h0.setposition(0,10)
            h0m2 = "Lucky for you, you had enough savings to pay for the treatment you needed.\nKeep this close brush with death in mind and make healthier decisions from now on!" 
            h0.write(h0m2, font=('Arial','12','normal'), align='center')
            time.sleep(7)
            h0.clear()
        else:
            h0.setposition(0,10)
            h0m2 = "Unfortunately, you weren't very thrifty either and cannot afford treatment.\nDeath awaits you. Goodbye."
            h0.write(h0m2, font=('Arial','12','normal'), align='center')
            time.sleep(3)
            h0.clear()
            game_over()           

    if default_attributes["money"] == 0:
        m0m1 = """You've run out of money and in a bid to regain your finances, decided to become a runner for a loan shark.
However, this doesn't come without risk. Will you get caught and sent to jail or make it out without repercussions?"""
        m0.setposition(0,110)
        m0.write(m0m1, font=('Arial','12','normal'), align='center')
        time.sleep(7)
        m0.setposition(0,75)
        m0.write("Let's see if it was worth it...", font=('Arial','11','normal'), align='center')
        time.sleep(3)
        randomOutcome = random.randint(1,100)
        # remainder 1: replenish, remainder 0: jail
        if randomOutcome % 2 == 1:
            default_attributes["money"] = 50
            m0.setposition(0,10)
            m0m2 = "Thank your lucky stars, you didn't get caught!\nTime to start making wiser spending decisions though..." 
            m0.write(m0m2, font=('Arial','12','normal'), align='center')
            time.sleep(5)
            m0.clear()
        else:
            m0.setposition(0,10)
            m0m2 = "Oh no, you got caught red-handed spray painting O$P$ signs on doors.\nIt's jail time for you!" 
            m0.write(m0m2, font=('Arial','12','normal'), align='center')
            time.sleep(5)
            m0.clear()
            game_over()

    if default_attributes["social"] == 0:
        s0m1 = """Your solitary lifestyle has taken a toll on your interpersonal relationships.
Your social life has been given a chance at revival by throwing a house party, at the expense of some of your health and money points."""
        s0.setposition(0,110)
        s0.write(s0m1, font=('Arial','12','normal'), align='center')
        time.sleep(6)
        s0.setposition(0,75)
        s0.write("Party ongoing... How well are you rebuilding your relationships?", font=('Arial','11','normal'), align='center')
        time.sleep(4)
        health = default_attributes["health"]
        money = default_attributes["money"]
        randomHPoints = random.randint(0, health)
        randomMPoints = random.randint(0, money)
        if randomHPoints < randomMPoints:
            randomPoints = random.randint(randomHPoints, randomMPoints)
        else: 
            randomPoints = random.randint(randomMPoints, randomHPoints)
        default_attributes["social"] += randomPoints
        default_attributes["health"] -= randomPoints
        default_attributes["money"] -= randomPoints
        s0.setposition(0,10)
        s0m2 = "The party was a success!\nTry to make some time for socialising to ensure your money and energy wasn't spent in vain though." 
        s0.write(s0m2, font=('Arial','12','normal'), align='center')
        time.sleep(7)
        s0.clear()

    if default_attributes["intelligence"] == 0:
        if default_attributes["social"] >= 50 or default_attributes["money"] >= 50:
            if default_attributes["social"] >= 50 and default_attributes["money"] >= 50:
                special_advantage = ", a little spare cash and your gift of gab"
            elif default_attributes["social"] >= 50:
                special_advantage = " and your gift of gab"
            else:
                special_advantage = " and a little spare cash"
            i0m1 = """Your grades have hit rock bottom and you're about to be expelled.
But wait! You find yourself in a room alone with the provost{}. You have one shot at bribing him to let you stay!""".format(special_advantage)
            i0.setposition(0,110)
            i0.write(i0m1, font=('Arial','12','normal'), align='center')
            time.sleep(7)
            i0.setposition(0,75)
            i0.write("Let's see if it was worth it...", font=('Arial','11','normal'), align='center')
            time.sleep(3)
            randomOutcome = random.randint(1,100)
            # remainder 1: stay in school, remainder 0: die
            if randomOutcome % 2 == 1:
                if default_attributes["social"] >= 50 and default_attributes["money"] >= 50:
                    default_attributes["intelligence"] = int(0.25 * default_attributes["social"]) + int(0.25 * default_attributes["money"])
                    default_attributes["social"] = int(0.75 * default_attributes["social"])
                    default_attributes["money"] = int(0.75 * default_attributes["money"])
                    i0.setposition(0,10)
                    i0m2 = "You let the money and your lips do the talking and successfully won the provost over. He has allowed you to continue your studies here.\nHow is your conscience holding up though? You probably shouldn't let this happen again. Study harder!"
                    i0.write(i0m2, font=('Arial','12','normal'), align='center')
                    time.sleep(9)
                    i0.clear()
                elif default_attributes["social"] >= 50:
                    default_attributes["intelligence"] = int(0.5 * default_attributes["social"])
                    default_attributes["social"] = int(0.5 * default_attributes["social"])
                    i0.setposition(0,10)
                    i0m2 = "You've successfully won the provost over with your smooth tongue. He has allowed you to continue your studies here.\nHow is your conscience holding up though? You probably shouldn't let this happen again. Study harder!"
                    i0.write(i0m2, font=('Arial','12','normal'), align='center')
                    time.sleep(9)
                    i0.clear()
                else:
                    default_attributes["intelligence"] = int(0.5 * default_attributes["money"])
                    default_attributes["money"] = int(0.5 * default_attributes["money"])
                    i0.setposition(0,10)
                    i0m2 = "Money makes the world go round. You've successfully won the provost over and he has allowed you to continue your studies here.\nHow is your conscience holding up though? You probably shouldn't let this happen again. Study harder!"
                    i0.write(i0m2, font=('Arial','12','normal'), align='center')
                    time.sleep(9)
                    i0.clear()
            else:
                i0.setposition(0,10)
                i0m2 = "You really thought that would work out? Bribery doesn't work here, but maybe you can bribe your way into another university.\nThat's right. You've been expelled."
                i0.write(i0m2, font=('Arial','12','normal'), align='center')
                time.sleep(8)
                i0.clear()
                game_over()
        else:
            i0m1 = """Your grades have hit rock bottom and you're about to be expelled.
But wait! You find yourself in a room alone with the provost. Maybe you should take a shot at bribing him to let you stay."""
            i0.setposition(0,110)
            i0.write(i0m1, font=('Arial','12','normal'), align='center')
            time.sleep(6)
            i0.setposition(0,75)
            i0.write("Calculating finances and social capability...", font=('Arial','11','normal'), align='center')
            time.sleep(3)
            i0.setposition(0,10)
            i0m2 = "Unfortunately, you aren't especially rich nor are you especially sociable... Oh well, there goes your chance.\nGet ready to be expelled. Goodbye."
            i0.write(i0m2, font=('Arial','12','normal'), align='center')
            time.sleep(6)
            i0.clear()
            game_over()

    bar_update(get_attribute_value())

### game over for when the player dies (any attribute = 0)
def game_over():
        finale.penup()
        finale.setpos(0,150)
        finale.write("GAME OVER", font=('Arial','40','bold'), align=('center'))
        finale.setpos(0,0)
        finale.write("SEEMS LIKE YOU COULD NOT TAKE THE PRESSURE", font=('Arial','25','bold'), align=('center'))
        finale.setpos(0,-40)
        finale.write("CLOSE THE GAME, YOU DISGUST ME", font=('Arial','20','bold'), align=('center'))
        turtle.done()

### setting up a random character and establishing initial default attributes for player
default_attributes = { "health": 50, "money": 50, "social": 50, "intelligence": 50}
characters = {1: "Healthy Hilary", 2: "Fat Frank", 3: "Rich Richard", 4: "Poor Pauline", 5: "Sociable Sam", 6: "Lonely Larry", 7: "Intelligent Iris", 8: "Unbright Ulya" }
assigned_character = random.randint(1,8)
assign_values(default_attributes, assigned_character)

## extract data from dictionary
char_name = characters[assigned_character]

### call function to update the attribute bars, takes in respective values of each attribute and chracter name
bar_initial_setup(get_attribute_value(), char_name)
#time.sleep(3)

### start of game, prompt player to enter yes to continue
answer = turtle.textinput("Are you ready?", "Enter 'yes' to start your SUTD journey")

### while loop forces player to type yes in order to continue
while True:
    if answer == 'yes':
        intro.undo()
        main.penup()
        break
    else:
        main.penup()
        main.setposition(-50,-50)
        main.write("Hey that's not nice.... \nBe a sport and give it a go", font=('Arial','20','bold'), align='center')
        answer = turtle.textinput("Are you ready?", "Enter 'yes' to start your SUTD journey")
        main.undo()

########################################## START OF PART-TIME VS UROP ###############################################################
main.setposition(-550,-50)
main.write("""You have been provided with an opportunity to undertake a UROP, or you can choose to spend your time working part-time, in order to keep your finances in check. 

What do you choose?



a. UROP 

b. Work part-time 

 """,font=('Arial','11','normal'))
time.sleep(3)
part_time = turtle.textinput("UROP or work?", "a. or b.")
main.undo()

while True:
    if part_time == 'a':
        default_attributes["intelligence"] += 10
        default_attributes["health"] -= 10
        choice_1 = "UROP"
        choice_2 = "working part-time"
        part_time = "1. You have chosen to sign up for a {} instead of {}. ".format(choice_1, choice_2)
        break

    if part_time == 'b':
        default_attributes["intelligence"] -= 10
        default_attributes["social"] -= 10
        default_attributes["money"] += 10
        choice_1 = "part-time job"
        choice_2 = "taking up a UROP"
        part_time = "1. You have chosen to sign up for a {} instead of {}. ".format(choice_1, choice_2)
        break
    else:
        main.write("""You have been provided with an opportunity to undertake a UROP, or you can choose to spend your time working part-time, in order to keep your finances in check. 

What do you choose?



a. UROP 

b. work part-time 

 """,font=('Arial','11','normal'))
        part_time = turtle.textinput("UROP or work?", "a. or b.")
        main.undo()
        
main.setposition(-575,-170)
main.write(part_time,font=('Arial','11','normal'))

### to reflect changes in attributes to bars
bar_update(get_attribute_value())
### to check if any attribute value is 0, if yes, launch random outcomes
check_attributes(default_attributes)
########################################## END OF PART-TIME VS UROP ###############################################################

########################################## START OF SUPPER VS SLEEP ###############################################################
main.setposition(-550,0)
main.write("""It's 11pm. Your friends have decided to go out for supper, and you have been invited.
'Sleep is for the weak!!' they say.

What do you choose?


a. Supper 

b. Sleep 
""",font=('Arial','11','normal'))
supper_sleep = turtle.textinput("To eat or sleep?", "a. or b.")
main.undo()

while True:
    if supper_sleep == 'a':
        default_attributes["social"] += 10
        default_attributes["money"] -= 15
        default_attributes["health"] -= 10
        supper_sleep = "2. You have chosen to go for supper and have fun, sacrificing your sleep."
        break

    if supper_sleep == 'b':
        default_attributes["social"] -= 20
        default_attributes["health"] += 5
        supper_sleep = "2. You have chosen to sleep instead of going for supper, where your friends are going to have fun."
        break
    
    else:
        main.write("""It's 11pm. Your friends have decided to go out for supper, and you have been invited.
'Sleep is for the weak!!' they say.

What do you choose?


a. Supper 

b. Sleep 
""",font=('Arial','11','normal'))
        supper_sleep = turtle.textinput("To eat or to sleep?", "a. or b.")
        main.undo()

main.setposition(-575,-200)
main.write(supper_sleep,font=('Arial','11','normal'))  

### to reflect changes in attributes to bars
bar_update(get_attribute_value())
### to check if any attribute value is 0, if yes, launch random outcomes
check_attributes(default_attributes)
########################################## END OF SUPPER VS SLEEP ###############################################################

########################################## START OF HELP FRIEND OR STUDY ALONE ###############################################################
main.setposition(-550,0)
main.write("""Your classmate has asked you to help him with a physics question which he has been struggling with for very long time.
However, you are in the midst of your revision and do not want to break the flow.

What do you choose? 


a. Help your friend 

b. Tell him you are busy and continue with your revision 
""",font=('Arial','11','normal'))
help_orstudy = turtle.textinput("Help a friend or act busy?", "a. or b.")
main.undo()

while True:
    if help_orstudy == 'a':
        default_attributes["social"] += 10
        default_attributes["intelligence"] += 5
        help_orstudy = "3. You have chosen to help your friend; you're a good lad."
        break

    if help_orstudy == 'b':
        default_attributes["social"] -= 20
        help_orstudy = "3. You have chosen your own utility over your friendship. Oh well..."
        guess_num_score1 = guess_num_game() ## start guess number game if choose b
        if guess_num_score1 == 1:
            default_attributes["intelligence"] += 5 ##if guess number, increase intelligence attribute
        else:
            default_attributes["intelligence"] -= 20
        break
        
    else:
        main.write("""Your classmate has asked you to help him with a physics question which he has been struggling with for very long time.
However, you are in the midst of your revision and do not want to break the flow.

What do you choose? 


a. Help your friend 

b. Tell him you are busy and continue with your revision 
""",font=('Arial','11','normal'))
        help_orstudy = turtle.textinput("Help a friend or act busy?", "a. or b.")
        main.undo()

main.setposition(-575,-230)
main.write(help_orstudy,font=('Arial','11','normal'))

### to reflect changes in attributes to bars
bar_update(get_attribute_value())
### to check if any attribute value is 0, if yes, launch random outcomes
check_attributes(default_attributes)
########################################## END OF HELP FRIEND OR STUDY ALONE ###############################################################

########################################## START OF CONFESS VS DON'T ###############################################################
main.setposition(-550,-20)
main.write("""You have had a crush on your friend for some time now.
You finally find yourself in a situation where you are alone with them and can tell them about your feelings.

What do you choose?


a. Confess and risk the friendship

b. Don’t confess and bottle your feelings up.
 
""",font=('Arial','11','normal'))
confess = turtle.textinput("Risk it all or conceal don't feel?", "a. or b.")
main.undo()

while True:
    if confess == 'a':
        confess = "confess."
        acceptance = random.randint(0,2)

        if acceptance == 0:
            confess = "4. Congrats! You're now in a relationship! Prepare to have fun and lose some money hehe"
            default_attributes["social"] += 10
            default_attributes["money"] -= 25
        else:
            confess = "4. You confessed but your friend isn't ready for the relationship. Try again next time buddy."
            default_attributes["health"] -= 20
        break

    if confess == 'b':
        default_attributes["social"] -= 15
        confess = "4. You chose to bottle up your feelings. Now you will never know..."
        break

    else:
        main.write("""You have had a crush on your friend for some time now.
You finally find yourself in a situation where you are alone with them and can tell them about your feelings.

What do you choose?


a. Confess and risk the friendship

b. Don’t confess and bottle your feelings up.
 
""",font=('Arial','11','normal'))
        confess = turtle.textinput("Risk it all or conceal don't feel?", "a. or b.")
        main.undo()

main.setposition(-575,-260)
main.write(confess,font=('Arial','11','normal'))

### to reflect changes in attributes to bars
bar_update(get_attribute_value())
### to check if any attribute value is 0, if yes, launch random outcomes
check_attributes(default_attributes)
########################################## END OF CONFESS VS DON'T ###############################################################

########################################## START OF DRINKING ###############################################################
main.setposition(-550,-20)
main.write("""It’s the middle of the week and it has been pretty hectic so far.
Your friends have decided to go drinking at Crooked Crooks, and have invited you as well.

What do you choose?


a. Go drinking

b. Stay in your room instead
 
""",font=('Arial','11','normal'))
drinking = turtle.textinput("Get wasted or be anti-social?", "a. or b.")
main.undo()

while True:
    if drinking == 'a':
        default_attributes["social"] += 10
        default_attributes["money"] -= 25
        default_attributes["health"] -= 10
        drinking = "5. You have chosen to relax and let loose for the night. Enjoy!"
        hangman_score = hangman_game(char_name) 
        if hangman_score == 1:
            default_attributes["social"] += 5
        else:
            default_attributes["health"] -= 20
        break

    if drinking == 'b':
        default_attributes["social"] -= 20
        default_attributes["health"] += 10
        default_attributes["money"] += 10
        drinking = "5. You have chosen to call it an early night and gone to bed. Rest well!"
        break

    else:
        main.write("""It’s the middle of the week and it has been pretty hectic so far.
Your friends have decided to go drinking at Crooked Crooks, and have invited you as well.

What do you choose?


a. Go drinking

b. Stay in your room instead
 
""",font=('Arial','11','normal'))
        drinking = turtle.textinput("Get wasted or be anti-social?", "a. or b.")
        main.undo()

main.setposition(-575,-290)
main.write(drinking,font=('Arial','11','normal'))

### to reflect changes in attributes to bars
bar_update(get_attribute_value())
### to check if any attribute value is 0, if yes, launch random outcomes
check_attributes(default_attributes)
########################################## END OF DRINKING ###############################################################

########################################## START OF DATE VS STUDY ###############################################################
main.setposition(-550,-40)
main.write("""Your friend wants to go on a full-day picnic on Saturday.
You have a lot of work to be done and midterms are coming up,
but at the same time, you have not really spent a lot of time with your friends lately.

What do you choose?


a. “Let’s go on a picnic”

b. “Sorry, I’ve got to do work today”
 
""",font=('Arial','11','normal'))
date_or_study = turtle.textinput("Date or schoolwork?", "a. or b.")
main.undo()

while True:
    if date_or_study == 'a':
        default_attributes["social"] += 10
        default_attributes["money"] -= 5
        default_attributes["intelligence"] -= 10
        date_or_study = "6. You have chosen to go on a date."
        break

    if date_or_study == 'b':
        default_attributes["social"] -= 20
        default_attributes["intelligence"] += 10
        default_attributes["health"] -= 10
        date_or_study = "6. You have chosen to study for midterms."
        break

    else:
        main.write("""Your girlfriend/boyfriend wants to go on a full-day picnic on Saturday.
You have a lot of work to be done and midterms are coming up,
but at the same time, you have not really spent a lot of time with your partner lately.

What do you choose?


a. “Let’s go on a picnic babe”

b. “Sorry babe, i’ve got to do work today”
 
""",font=('Arial','11','normal'))
        date_or_study = turtle.textinput("Date or schoolwork?", "a. or b.")
        main.undo()

main.setposition(-575,-320)
main.write(date_or_study,font=('Arial','11','normal'))

### to reflect changes in attributes to bars
bar_update(get_attribute_value())
### to check if any attribute value is 0, if yes, launch random outcomes
check_attributes(default_attributes)
########################################## END OF DATE VS STUDY ###############################################################

########################################## START OF SLEEP IN OR STUDY ###############################################################
main.setposition(-550,-40)
main.write("""
The alarm rings at 7am.
You had planned to wake up early to get some work done before the hectic day begins.
However, you are feeling extremely sleepy and tired, and are really tempted to sleep in for another 2 hours.

What do you choose?


a. Get grinding mate!! You snooze you lose

b. I need my beauty sleep
 
""",font=('Arial','11','normal'))
sleep_in = turtle.textinput("Bookz or snooze?", "a. or b.")
main.undo()

while True:
    if sleep_in == 'a':
        default_attributes["health"] -= 20
        default_attributes["intelligence"] += 10
        sleep_in = "7. You have chosen the grind life. Hard worker!"
        break

    if sleep_in == 'b':
        default_attributes["health"] += 10
        default_attributes["intelligence"] -= 15
        sleep_in = "7. You have chosen to get your beauty sleep. Rest well while you can!"
        break

    else:
        main.write("""
The alarm rings at 7am.
You had planned to wake up early to get some work done before the hectic day begins.
However, you are feeling extremely sleepy and tired, and are really tempted to sleep in for another 2 hours.

What do you choose?


a. Get grinding mate!! You snooze you lose

b. I need my beauty sleep
 
""",font=('Arial','11','normal'))
        sleep_in = turtle.textinput("Bookz or snooze?", "a. or b.")
        main.undo()

main.setposition(100,-170)
main.write(sleep_in,font=('Arial','11','normal'))

### to reflect changes in attributes to bars
bar_update(get_attribute_value())
### to check if any attribute value is 0, if yes, launch random outcomes
check_attributes(default_attributes)
########################################## END OF SLEEP IN OR STUDY ###############################################################

########################################## START OF GAME OR GYM  ###############################################################
main.setposition(-550,-40)
main.write("""You’ve had a long day and really need to destress.
You haven’t been to the gym in a while and you really feel like you need a work out.
On the other hand, you could comfortably playing some video games with your friends.

What do you choose? 


a. Destroy some weights in the gym

b. Destroy my friends in game.

""",font=('Arial','11','normal'))
gym = turtle.textinput("Get ripped or get rekt?", "a. or b.")
main.undo()

while True:
    if gym == 'a':
        default_attributes["health"] += 10
        gym = "8. You have chosen to destroy some weights. Go get them man!"
        break

    if gym == 'b':
        default_attributes["social"] += 10
        default_attributes["health"] -= 15
        gym = "8. You have chosen to slay some dragons. Hope they don't eat you!"
        break

    else:
        main.write("""You’ve had a long day and really need to destress.
You haven’t been to the gym in a while and you really feel like you need a work out.
On the other hand, you could comfortably playing some video games with your friends.

What do you choose? 


a. Destroy some weights in the gym

b. Destroy my friends in game.

""",font=('Arial','11','normal'))
        gym = turtle.textinput("Get ripped or get rekt?", "a. or b.")
        main.undo()

main.setposition(100,-200)
main.write(gym,font=('Arial','11','normal'))

### to reflect changes in attributes to bars
bar_update(get_attribute_value())
### to check if any attribute value is 0, if yes, launch random outcomes
check_attributes(default_attributes)
########################################## END OF GAME OR GYM  ###############################################################

########################################## START OF STAYCATION VS CAMP ###############################################################
main.setposition(-550,-40)
main.write("""It is finally week 7, recess week.
Your family wants to go on a staycation so that you can relax from the stresses of university life.
On the other hand, your fifth-row has a 3-day camp coming up, where you will be having some intense but fun training.

What do you choose?


a. Bali vibes mate

b. Fifth-row is my life mate
 
""",font=('Arial','11','normal'))
staycation = turtle.textinput("Vacay or camp?", "a. or b.")
main.undo()

while True:
    if staycation == 'a':
        default_attributes["money"] -= 30
        default_attributes["intelligence"] -= 15
        default_attributes["social"] += 15
        default_attributes["health"] += 15
        staycation = "9. You have chosen to have fun in Bali. Don't party too hard! :P"
        break

    if staycation == 'b':
        default_attributes["social"] += 25
        default_attributes["intelligence"] += 10
        default_attributes["money"] += 20
        staycation = "9. You have chosen to have fun in Changi instead of Bali. O man..."
        break

    else:
        main.write("""It is finally week 7, recess week.
Your family wants to go on a staycation so that you can relax from the stresses of university life.
On the other hand, your fifth-row has a 3-day camp coming up, where you will be having some intense but fun training.

What do you choose?


a. Bali vibes mate

b. Fifth-row is my life mate
 
""",font=('Arial','11','normal'))
        staycation = turtle.textinput("Vacay or camp?", "a. or b.")
        main.undo()

main.setposition(100,-230)
main.write(staycation,font=('Arial','11','normal'))

### to reflect changes in attributes to bars
bar_update(get_attribute_value())
### to check if any attribute value is 0, if yes, launch random outcomes
check_attributes(default_attributes)
########################################## END OF STAYCATION VS CAMP ###############################################################

########################################## START OF EXCO VS SLACKER  ###############################################################
main.setposition(-550,-40)
main.write("""Your fifth-row camp has ended and the time has come to choose whether you want to be an EXCO member in your fifth-row.
On one hand, you want to serve your friends and hone your leadership skills.
On the other, you just want to have fun and not indulge yourself in responsibilities.

What do you choose?


a. Service is in my blood

b. Nah man just wanna have fun.
 
""",font=('Arial','11','normal'))
exco_or = turtle.textinput("EXCO or lepak?", "a. or b.")
main.undo()

while True:
    if exco_or == 'a':
        default_attributes["health"] -= 20
        default_attributes["intelligence"] += 10
        default_attributes["social"] += 10
        exco_or = "10. You have chosen to serve to the best of your abilities. All the best!"
        break

    if exco_or == 'b':
        default_attributes["health"] += 15
        exco_or = "10. You have chosen to be a slacker fella. Life's too short for responsibilities :P"
        break

    else:
        main.write("""Your fifth-row camp has ended and the time has come to choose whether you want to be an EXCO member in your fifth-row.
On one hand, you want to serve your friends and hone your leadership skills.
On the other, you just want to have fun and not indulge yourself in responsibilities.

What do you choose?


a. Service is in my blood

b. Nah man just wanna have fun.
 
""",font=('Arial','11','normal'))
        exco_or = turtle.textinput("EXCO or lepak?", "a. or b.")
        main.undo()

main.setposition(100,-260)
main.write(exco_or,font=('Arial','11','normal'))

### to reflect changes in attributes to bars
bar_update(get_attribute_value())
### to check if any attribute value is 0, if yes, launch random outcomes
check_attributes(default_attributes)
########################################## END OF EXCO VS SLACKER  ###############################################################

########################################## START OF HOME ON WEEKENDS OR STAY IN HOSTEL  ###############################################################
main.setposition(-550,-30)
main.write("""Finals week is coming up and your productivity during the weekends at home have been very low over the past few weeks.

What do you choose?


a. Go home on the weekend

b. Stay in hostel
 
""",font=('Arial','11','normal'))
gohome_or = turtle.textinput("Home or hostel?", "a. or b.")
main.undo()

while True:
    if gohome_or == 'a':
        default_attributes["intelligence"] -= 10
        default_attributes["social"] += 5
        default_attributes["health"] += 5
        gohome_or = "11. You have chosen to go home and relax a little. Good for you!"
        break

    if gohome_or == 'b':
        default_attributes["social"] -= 10
        default_attributes["intelligence"] += 10
        default_attributes["health"] -= 15
        gohome_or = "11. You have chosen to care more about the grind. Don't burn out!"
        break

    else:
        main.write("""Finals week is coming up and your productivity during the weekends at home have been very low over the past few weeks.

What do you choose?


a. Go home on the weekend

b. Stay in hostel
 
""",font=('Arial','11','normal'))
        gohome_or = turtle.textinput("Home or hostel?", "a. or b.")
        main.undo()

main.setposition(100,-290)
main.write(gohome_or,font=('Arial','11','normal'))

### to reflect changes in attributes to bars
bar_update(get_attribute_value())
### to check if any attribute value is 0, if yes, launch random outcomes
check_attributes(default_attributes)
########################################## END OF HOME ON WEEKENDS OR STAY IN HOSTEL  ###############################################################

########################################## START OF FINALS VS 2D   ###############################################################
main.setposition(-550,-40)
main.write("""The dreaded 2D project brief has been released.
There is so much to do that you and your group mates have no idea where to even start.
To make things worse, it is finals right after the submission dates of the various 2D projects.
Part of you just wants to let your group mates do all the work and focus on your finals, 
given how you have been failing all your subjects so far.

What do you choose?


a. Be a lad and help your group mates out

b. My grades are more important to me. Let me take the exam now!

c. I think I will be able to do both. Let's do it bro! 
 
""",font=('Arial','11','normal'))
finals_or_2d = turtle.textinput("Tough decision bro", "a. or b. or c.")
main.undo()

while True:
    if finals_or_2d == 'a':
        default_attributes["intelligence"] += 5
        default_attributes["social"] += 5
        finals_or_2d = "12. You have chosen to be a team player. Well done!"
        exam_score_display.penup()
        exam_score_display.setpos(-125,100)
        score_message = """Term 1 draws to a close
and you let out a heavy sigh...
Congrats on surviving Term 1!
Ready to see your final stats?"""
        exam_score_display.write(score_message,font=('Arial','15','normal'))
        break

    if finals_or_2d == 'b':
        default_attributes["social"] -= 20
        default_attributes["intelligence"] += 10
        finals_or_2d = "12. You have chosen to focus on yourself. (hmm... selfish...)"
        exam_score = draw_exam_paper()
        if exam_score == 3:
            default_attributes["intelligence"] += 10
            exam_score_display.penup()
            exam_score_display.setpos(-125,100)
            score_message = """You have scored 3/3!
Congrats on surviving finals!

Ready to see your final stats?"""
            exam_score_display.write(score_message,font=('Arial','15','normal'))
        elif exam_score == 2:
            default_attributes["intelligence"] -= 10
            exam_score_display.penup()
            exam_score_display.setpos(-125,100)
            score_message = """You have scored 2/3!
Congrats on surviving finals!

Ready to see your final stats?"""
            exam_score_display.write(score_message,font=('Arial','15','normal'))
        elif exam_score == 1:
            default_attributes["intelligence"] -= 15
            exam_score_display.penup()
            exam_score_display.setpos(-125,100)
            score_message = """You have scored 1/3...
Did you even study for your finals!

Nevermind...
You will always pass failure
on your way to success!
Ready to see your final stats?"""
            exam_score_display.write(score_message,font=('Arial','15','normal'))
        else:
            default_attributes["intelligence"] -= 25
            exam_score_display.penup()
            exam_score_display.setpos(-125,100)
            score_message = """You have scored 0...
Did you even study for your finals?

Nevermind...
You will always pass failure 
on your way to success!
Ready to see your final stats?"""
            exam_score_display.write(score_message,font=('Arial','15','normal'))
        break

    if finals_or_2d == 'c':
        default_attributes["social"] -= 10
        default_attributes["intelligence"] -= 5
        finals_or_2d = "12. You have chosen to be greedy and lost some points. Serves you right!"
        exam_score = draw_exam_paper()
        if exam_score == 3:
            default_attributes["intelligence"] += 10
            exam_score_display.penup()
            exam_score_display.setpos(-125,100)
            score_message = """You have scored 3/3!
Congrats on surviving finals!
Ready to see your final stats?"""
            exam_score_display.write(score_message,font=('Arial','15','normal'))
        elif exam_score == 2:
            default_attributes["intelligence"] -= 10
            exam_score_display.penup()
            exam_score_display.setpos(-125,100)
            score_message = """You have scored 2/3!
Congrats on surviving finals!
Ready to see your final stats?"""
            exam_score_display.write(score_message,font=('Arial','15','normal'))
        elif exam_score == 1:
            default_attributes["intelligence"] -= 15
            exam_score_display.penup()
            exam_score_display.setpos(-125,100)
            score_message = """You have scored 1/3...
Did you even study for your finals?

Nevermind...
You will always pass failure
on your way to success!
Ready to see your final stats?"""
            exam_score_display.write(score_message,font=('Arial','15','normal'))
        else:
            default_attributes["intelligence"] -= 25
            exam_score_display.penup()
            exam_score_display.setpos(-125,100)
            score_message = """You have scored 0...
Did you even study for your finals?

Nevermind...
You will always pass failure 
on your way to success!
Ready to see your final stats?"""
            exam_score_display.write(score_message,font=('Arial','15','normal'))
        break

    else:
        main.write("""The dreaded 2D project brief has been released.
There is so much to do that you and your group mates have no idea where to even start.
To make things worse, it is finals right after the submission dates of the various 2D projects.
Part of you just wants to let your group mates do all the work and focus on your finals, 
given how you have been failing all your subjects so far.

What do you choose?


a. Be a lad and help your group mates out

b. My grades are more important to me. Let me take the exam now!

c. I think I will be able to do both. Lets do it bro! 
 
""",font=('Arial','11','normal'))
        finals_or_2d = turtle.textinput("Tough decision bro", "a. or b. or c.")
        main.undo()

main.setposition(100,-320)
main.write(finals_or_2d,font=('Arial','11','normal'))

### to reflect changes in attributes to bars
bar_update(get_attribute_value())
### to check if any attribute value is 0, if yes, launch random outcomes
check_attributes(default_attributes)
########################################## END OF FINALS VS 2D   ###############################################################

results = turtle.textinput("Time to get your results", "Enter 'yes' to get your results")
while True:
    if results == 'yes':
        exam_score_display.undo()
        display_finale(get_attribute_value())
        break

    else:
        results = turtle.textinput("Time to get your results", "Enter 'yes' to get your results")

end = turtle.textinput("The end", "Enter 'yes' to continue")
while True:
    if end == 'yes':
        finale.clear()
        thank_you()
        break
    else:
        end = turtle.textinput("The end", "Enter 'yes' to continue")

turtle.done()