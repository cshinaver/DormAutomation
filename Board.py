import RPi.GPIO as GPIO


class Board:
    BUTTON_1_PIN = 8
    LED_PIN = 10
    OUTLET_PIN = 12
    is_led_on = 0
    is_outlet_on = 0

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.BUTTON_1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.LED_PIN, GPIO.OUT)
        GPIO.setup(self.OUTLET_PIN, GPIO.OUT)

        GPIO.output(self.LED_PIN, self.is_led_on)
        GPIO.output(self.OUTLET_PIN, self.is_outlet_on)

    def start_interrupts(self):
        # Button 1 interrupt
        #GPIO.add_event_detect(
        #    self.BUTTON_1_PIN,
        #    GPIO.FALLING,
        #    callback=self.button_1_callback,
        #    bouncetime=200
        #)

    def button_1_callback(self, channel):
        print "Button 1 interrupt triggered"
        self.toggle_led()

    def toggle_led(self):
        if (self.is_led_on):
            self.is_led_on = 0
        else:
            self.is_led_on = 1
        GPIO.output(self.LED_PIN, self.is_led_on)

    def toggle_outlet(self):
        if (self.is_outlet_on):
            self.is_outlet_on = 0
        else:
            self.is_outlet_on = 1
        GPIO.output(self.OUTLET_PIN, is_outlet_on)


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
