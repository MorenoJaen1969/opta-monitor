import serial
import time
import requests
import sys

SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 9600
API_URL = 'http://localhost/opta-monitor/api/save.php'

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    print(f"Conectado a {SERIAL_PORT}")
except serial.SerialException as e:
    print(f"Error al abrir el puerto serial: {e}")
    sys.exit(1)

buffer = { 'I1': None, 'I2': None, 'I3': None }

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        if line.startswith('I') and 'value:' in line:
            parts = line.split()
            terminal = parts[0].rstrip(':')
            value = int(parts[-1])
            if terminal in buffer:
                buffer[terminal] = value
                if all(v is not None for v in buffer.values()):
                    data = { 'i1': buffer['I1'], 'i2': buffer['I2'], 'i3': buffer['I3'] }
                    try:
                        resp = requests.post(API_URL, data=data, timeout=3)
                        if resp.text.strip() == "OK":
                            print(f"✓ Enviado: {data}")
                        else:
                            print(f"⚠ Error en respuesta: {resp.text}")
                    except Exception as e:
                        print(f"✗ Error al enviar: {e}")
                    buffer = { 'I1': None, 'I2': None, 'I3': None }
    except Exception as e:
        print(f"Error de lectura: {e}")
        time.sleep(1)
