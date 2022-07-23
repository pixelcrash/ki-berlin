from escpos.printer import Usb

#printer = Usb(0x0416, 0x5011, profile="POS-5890")

p = Usb(0x0483,0x5743)
# Print text
p.text("Hello World\n")
p.cut()
