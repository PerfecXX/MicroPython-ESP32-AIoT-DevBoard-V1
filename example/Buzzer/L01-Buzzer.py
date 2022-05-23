# ---Import Library---
from machine import Pin,PWM
from time import sleep

# ---Pin Setup---
buzzer_Pin = Pin(32,Pin.OUT)
freq = 3000                       # If the frequency is high, there will be a squealing sound.
duty = 1000                       # Volume level

# ---Main Program---
beep = PWM(buzzer_Pin,freq,duty)  # Play Buzzer with frequency,duty cycle 
sleep(0.5)                        # Beep length
beep.deinit()                     # Stop Playing



