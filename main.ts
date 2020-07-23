function faireQuelqueChose () {
    if (y1 == 4 && x == x1) {
        score += 1
        y1 = 0
        x1 = randint(0, 4)
    } else if (y1 == 4 && x != x1) {
        basic.clearScreen()
        basic.showString("Score:")
        basic.showNumber(score)
        control.reset()
    }
    led.plot(x1, y1)
    basic.pause(300)
    led.unplot(x1, y1)
    y1 += 1
    led.plot(x1, y1)
}
input.onButtonPressed(Button.A, function () {
    led.unplot(x, y)
    x += -1
    if (x < 0) {
        x = 0
    }
    led.plot(x, y)
})
input.onButtonPressed(Button.B, function () {
    led.unplot(x, y)
    x += 1
    if (x > 4) {
        x = 4
    }
    led.plot(x, y)
})
let y1 = 0
let x = 0
let score = 0
let y = 0
let x1 = 0
x1 = randint(0, 4)
y = 4
score = 0
led.plot(x, y)
basic.forever(function () {
    faireQuelqueChose()
})
