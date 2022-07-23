from escpos.connections import getUSBPrinter


printer = getUSBPrinter()(idVendor=0x0483,
                          idProduct=0x5743,
                          inputEndPoint=0x82,
                          outputEndPoint=0x01) # Create the printer object with the connection params

printer.text("Hello World")
printer.lf()
