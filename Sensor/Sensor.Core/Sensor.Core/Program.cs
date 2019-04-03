using System;
using System.Runtime.InteropServices;

namespace Sensor.Core
{
    class Program
    {
        private static int OPEN_READ_WRITE = 2;
        private static int I2C_SLAVE = 0x0703;

        [DllImport("libc.so.6", EntryPoint = "open")]
        public static extern int Open(string fileName, int mode);

        [DllImport("libc.so.6", EntryPoint = "ioctl", SetLastError = true)]
        private extern static int Ioctl(int fd, int request, int data);

        [DllImport("libc.so.6", EntryPoint = "read", SetLastError = true)]
        internal static extern int Read(int handle, byte[] data, int length);

        static void Main(string[] args)
        {
            // read from I2C device bus 1
            var i2cBushandle = Open("/dev/i2c-1", OPEN_READ_WRITE);

            // open the slave device at address 0x68 for communication
            int registerAddress = 0x68;
            var deviceReturnCode = Ioctl(i2cBushandle, I2C_SLAVE, registerAddress);

            // read the first two bytes from the device into an array
            var deviceDataInMemory = new byte[2];
            Read(i2cBushandle, deviceDataInMemory, deviceDataInMemory.Length);

            Console.WriteLine($"Most significant byte = {deviceDataInMemory[0]}");
            Console.WriteLine($"Least significant byte = {deviceDataInMemory[1]}");
        }
    }
}
