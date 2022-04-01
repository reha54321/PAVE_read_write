from machine import I2C
from hmc5883l import HMC5883L
from time import sleep
from bn880 import BN880
from HumPro import humPro
# Please check that correct PINs are set on hmc5883l library!
compass = HMC5883L()
gps = BN880()
rf = humPro(
    crespPin=27, bePin=21, cmdPin=26, ctsPin=22, txPin=16, rxPin=17, modeIndPin=18
)
BUTTON = machine.Pin(14, machine.Pin.IN,machine.Pin.PULL_DOWN)  # button pin
BUTTON.irq(trigger=Pin.IRQ_RISING, handler=rf.transmitRandNumber)
rf.CRESP.irq(trigger=Pin.IRQ_RISING, handler=rf.readData)
while True:
    sleep(0.5)
    x, y, z = compass.read()
    print(compass.heading(x, y))
    print(gps.toString())
    rf.transmitData(gps.toString() + ", (" + str(compass.heading(x,y)[0]) + ", " + str(compass.heading(x,y)[1])  + ")")
    
    controlString = rf.readData()
    print(controlString)
