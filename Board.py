import RPi.GPIO as GPIO


class Board:
    BUTTON_1_PIN = 8
    LED_PIN = 10
    LED_isLit = 0

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.BUTTON_1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.LED_PIN, GPIO.OUT)

    def start_interrupts(self):
        # Button 1 interrupt
        GPIO.add_event_detect(
            self.BUTTON_1_PIN,
            GPIO.FALLING,
            callback=self.button_1_callback,
            bouncetime=200
        )

    def button_1_callback(self, channel):
        print "Button 1 interrupt triggered"
        self.toggle_led()

    def toggle_led(self):
        if (self.LED_isLit):
            self.LED_isLit = 0
        else:
            self.LED_isLit = 1
        GPIO.output(self.LED_PIN, self.LED_isLit)


# Testing
if __name__ == "__main__":
    bae_board = Board()
    bae_board.start_interrupts()
    try:
        while (1):
            pass
    except KeyboardInterrupt:
        GPIO.cleanup()
    GPIO.cleanup()
