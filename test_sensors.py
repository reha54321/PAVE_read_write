from machine import I2C
from hmc5883l import HMC5883L
from time import sleep
from bn880 import BN880

# Please check that correct PINs are set on hmc5883l library!
sensor = HMC5883L()
gps = BN880()

while True:
    sleep(0.5)
    x, y, z = sensor.read()
    print(sensor.format_result(x, y, z))
    print(gps.read())