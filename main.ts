basic.forever(function () {
    basic.showIcon(IconNames.Heart)
    led.setBrightness(255 - input.lightLevel())
})
