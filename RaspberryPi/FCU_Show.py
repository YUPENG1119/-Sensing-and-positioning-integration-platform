import i2c_driver

mylcd = i2c_driver.LCD()

mylcd.lcd_display_string("Welcome FCU!", 1)
mylcd.lcd_display_string("Feng Cheng Lin", 2)

# sudo i2cdetect -y 1