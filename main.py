def on_button_pressed_a():
    basic.show_leds("""
        . # . # .
                . . . . .
                # . . . #
                . # # # .
                . . . . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        . # . # .
                . . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . # . # .
                . . . . .
                . # # # .
                # . . . #
                . . . . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("Hi")

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    basic.show_string("Todey we gonna do a tetorial off smille. :)!")
basic.forever(on_forever2)
