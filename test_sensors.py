from machine import I2C
from hmc5883l import HMC5883L
from time import sleep
from bn880 import BN880

# Please check that correct PINs are set on hmc5883l library!
compass = HMC5883L()
gps = BN880()
rf = humPro(crespPin=32, bePin = 27, cmdPin = 31, ctsPin = 29, txPin = 31, rxPin = 22, modeIndPin = 24, buttonPin = 9)

rf.CRESP.irq(trigger=Pin.IRQ_RISING, handler=self.readData)
rf.BUTTON.irq(trigger=Pin.IRQ_RISING, handler=self.transmitRandNumber)

while True:
    sleep(0.5)
    x, y, z = compass.read()
    print(compass.format_result(x, y, z))
    print(gps.read())
