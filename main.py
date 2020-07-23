def on_button_pressed_a():
    global x
    led.unplot(x, y)
    x += -1
    if x < 0:
        x = 0
    led.plot(x, y)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global x
    led.unplot(x, y)
    x += 1
    if x > 4:
        x = 4
    led.plot(x, y)
input.on_button_pressed(Button.B, on_button_pressed_b)

x2 = 0
y1 = 0
x = 0
y = 0
x1 = randint(0, 4)
y = 4
score = 0
led.plot(x, y)

def on_forever():
    global score, y1, x1, x2
    if y1 == 4 and x == x1:
        score += 1
        y1 = 0
        basic.pause(500)
        x1 = randint(0, 4)
    elif y1 == 4 and x != x1:
        basic.clear_screen()
        basic.show_string("Score:")
        basic.show_number(score)
    led.plot(x1, y1)
    basic.pause(500)
    led.unplot(x1, y1)
    y1 += 1
    led.plot(x1, y1)
    if y1 == 3:
        y2 = 0
        x2 = randint(0, 4)
        led.plot(x2, y2)
basic.forever(on_forever)
