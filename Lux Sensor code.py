import smbus
import time

bus = smbus.SMBus(1)

bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)

bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

time.sleep(0.5)

while True:
    
    data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)   
    data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)   
    
    ch0 = data[1] * 256 + data[0]
    ch1 = data1[1] * 256 + data1[0]
  
    print("Full Spectrum(IR + Visible) :%d lux" % ch0)
    print("Infrared Value :%d lux" % ch1)
    print("Visible Value :%d lux" % (ch0 - ch1))

    time.sleep(1)