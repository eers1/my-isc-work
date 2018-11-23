from datetime import datetime
import serial
import io

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 9600,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE
)

sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding = 'ascii', newline = '\r')
sio._CHUNK_SIZE = 1

with open("TempOutput", 'a') as f:
    while ser.isOpen():
        datastring = sio.readline()
        f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n')
        f.flush()



ser.close()


