import serial

for i in range(256):
    try:
        s = serial.Serial(i)
        
        s.write("{NAME=Nick}")
        s.close()
    except serial.SerialException:
        pass