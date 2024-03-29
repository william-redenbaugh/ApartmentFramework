import time
import socket

import led_control

strip_one = None
UDP_IP = "192.168.86.204"
UDP_PORT = 5050

sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
strip_one = led_control.LEDStrip(0, 650, sending_socket, UDP_IP, UDP_PORT)

def run_leds():
    global strip_one

    for i in range(650):
        strip_one.set_led(150, 15, 150, i)
        strip_one.send_dat()
        time.sleep(.01)
        
    for i in range(650):
        strip_one.set_led(0, 0, 0, i)
        strip_one.send_dat()
        time.sleep(.01)


def main():
    while(1):
        run_leds()

main()
