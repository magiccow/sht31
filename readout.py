import board
import busio
import adafruit_sht31d
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c, 0x45)

while True:
  print('Temp = {:.1f} \u00B0C'.format(sensor.temperature))
  print('RH = {:.1f} %\n'.format(sensor.relative_humidity))
  time.sleep(2)
