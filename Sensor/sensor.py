import smbus
from time import sleep
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

# Constants - MPU6050 Registers and addresses
PWR_MGMT_1 =    0x6B
SMPLRT_DIV =    0x19
CONFIG =        0x1A
GYRO_CONFIG =   0x1B
INT_ENABLE =    0x38
ACCEL_XOUT_H =  0x3B
ACCEL_YOUT_H =  0x3D
ACCEL_ZOUT_H =  0x3F
GYRO_XOUT_H =   0x43
GYRO_YOUT_H =   0x45
GYRO_ZOUT_H =   0x47



def MPU_Init():
    # Write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, )

    # Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

    # Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)

    # Write to Gyro Configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

    # Write to Interrupt Enable Register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    # 16-bit Accelerometer and Gyroscope values:
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)

    value = ((high << 8) | low)

    if (value > 23768):
        value = value - 65536
    return value

bus = smbus.SMBus(1)
Device_Address = 0x68
keep_running = True
while keep_running:
    try:
        accel_x = read_raw_data(ACCEL_XOUT_H)
        accel_y = read_raw_data(ACCEL_YOUT_H)
        accel_z = read_raw_data(ACCEL_ZOUT_H)

        gyro_x = read_raw_data(GYRO_XOUT_H)
        gyro_y = read_raw_data(GYRO_YOUT_H)
        gyro_z = read_raw_data(GYRO_ZOUT_H)
        sys.stdout.write("\rAcc: " + str(accel_x) + ", " + str(accel_y) + ", " + str(accel_z))
        sys.stdout.write("\nGyro: " + str(gyro_x) + ", " + str(gyro_y) + ", " + str(gyro_z))
        sys.stdout.flush()
    except KeyboardInterrupt:
        keep_running = False
        print("bye bye!")
