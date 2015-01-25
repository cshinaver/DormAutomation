import RPi.GPIO as GPIO


class Board:
    LED_PIN = 10
    OUTLET_PIN = 12
    STROBE_PIN = 8
    is_led_on = 0
    is_outlet_on = 0
    is_strobing = 0

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(self.BUTTON_1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.STROBE_PIN, GPIO.OUT)
        GPIO.setup(self.LED_PIN, GPIO.OUT)
        GPIO.setup(self.OUTLET_PIN, GPIO.OUT)

        GPIO.output(self.LED_PIN, self.is_led_on)
        GPIO.output(self.OUTLET_PIN, self.is_outlet_on)
        GPIO.output(self.STROBE_PIN, self.is_strobing)

    def start_interrupts(self):
        pass
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
        GPIO.output(self.OUTLET_PIN, self.is_outlet_on)

    def toggle_strobe(self):
        if (self.is_strobing):
            self.is_strobing = 0
        else:
            self.is_strobing = 1
        GPIO.output(self.STROBE_PIN, is_strobing)

    def cleanup(self):
        GPIO.cleanup()


# Testing
if __name__ == "__main__":
    bae_board = Board()
    bae_board.start_interrupts()
    bae_board.toggle_outlet()
    try:
        while (1):
            pass
    except KeyboardInterrupt:
        GPIO.cleanup()
    GPIO.cleanup()
