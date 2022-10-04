radio.onReceivedNumber(function (receivedNumber) {
    basic.showNumber(receivedNumber)
})
input.onButtonPressed(Button.A, function () {
    tal += 1
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(tal)
})
input.onButtonPressed(Button.B, function () {
    tal = 0
})
let tal = 0
radio.setGroup(12)
basic.forever(function () {
    basic.showNumber(tal)
})
