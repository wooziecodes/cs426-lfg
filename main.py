def on_forever():
    basic.show_icon(IconNames.HEART)
    led.set_brightness(input.light_level())
basic.forever(on_forever)
