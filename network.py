# Mesh network handling application
import time
import serial
import platform
import glob

# Global constants
PORT = "/dev/ttyS31"
BAUD_RATE = 9600
PARITY = serial.PARITY_EVEN
STOP_BITS = 2
BYTE_SIZE = 8

def main():
    s = init()
    if s != None:
        #s.open()
        while True:
            print(s.readline())






# Gets user input to initialize the serial port
def init():
    port = PORT
    rate = BAUD_RATE
    parity = PARITY
    stopBits = STOP_BITS
    byteSize = BYTE_SIZE

    # get all available ports
    ports = list_ports()
    
    # ask user which port to use
    print("List of ports:\n")
    i = 1
    for port in ports:
        print("\t" + str(i) + ": " + str(port))
        i += 1
    print("")

    inputPort = None
    while inputPort == None:
        inputPort = raw_input("Enter a port to use: ")
        try:
            inputPort = int(inputPort)
            if inputPort >= i or inputPort < 1:
                inputPort = None
        except:
            inputPort = None

    port = ports[inputPort - 1]
    print("\nUsing port " + port + ".\n")
    inputRate =  raw_input("Use baud rate of " + str(rate) + "? (Y/N): ")
    if inputRate.upper() != "Y":
        newRate = raw_input("Enter new rate: ")
        try:
            rate = int(newRate)
        except:
            print("Invalid rate.")
    print("Using baud rate " + str(rate) + ".\nInitializing serial...\n")
        
    s = get_serial(port, rate, parity, stopBits, byteSize)
    return s

# Lists all serial ports in a cross-platform fashion.
def list_ports():
    ports = None
    if platform.system() == "Windows":
        ports = []
        for i in range(256):
            try:
                s = serial.Serial(i)
                ports.append(i)
                s.close()
            except serial.SerialException:
                pass
    else:
        ports = glob.glob("/dev/ttyS*") + glob.glob("/dev/ttyUSB*")

    return ports

# Returns a serial object with selected parameters
def get_serial(port = PORT, rate = BAUD_RATE, parity = PARITY,
               stopBits = STOP_BITS, byteSize = BYTE_SIZE):

    # track whether an error occurs
    error = False

    # convert stop bits to acceptable value
    if float(stopBits) == 1.0:
        stopBits = serial.STOPBITS_ONE
    elif float(stopBits) == 1.5:
        stopBits = serial.STOPBITS_ONE_POINT_FIVE
    elif float(stopBits) == 2.0:
        stopBits = serial.STOPBITS_TWO
    else:
        print("Error: Invalid stop bits.")
        error = True

    # convert byte size to acceptable value
    if byteSize == 5:
        byteSize = serial.FIVEBITS
    elif byteSize == 6:
        byteSize = serial.SIXBITS
    elif byteSize == 7:
        byteSize = serial.SEVENBITS
    elif byteSize == 8:
        byteSize = serial.EIGHTBITS
    else:
        print("Error: Invalid byte size.")
        error = True

    # try to create the serial object
    s = None
    try:
        s = serial.Serial(port, rate, byteSize, parity, stopBits)
    except:
        print("Error: serial could not be initialized.")
        error = True

    # return the serial object if no errors occurred
    if error:
        return None
    else:
        return s

# call main function
if __name__ == "__main__":
    main()