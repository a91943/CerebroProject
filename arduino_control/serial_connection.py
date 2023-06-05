import serial

# Initialize Serial (conficuration)
def initSerial():
    global ser  # Serial Object
    ser = serial.Serial('COM4',    # The COM changes with differentn boards and PCs
                    baudrate=115200,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=12)

# Close Serial Connection with Arduino
def closeSerial():
    global ser
    if 'ser' in globals():
        ser.close()
        print("Porta Serie Fechada")
    else:
        print("Porta Serie Aberta")

def sendMessage(message):
    ser.write(message.encode())


initSerial()
sendMessage("HelloWorld!")
print("mensagem enviada")
closeSerial()