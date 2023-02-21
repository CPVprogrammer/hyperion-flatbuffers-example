'''
		Hyperion - flatbuffers
'''
import time
import io

from hyperion import Hyperion
from colour import Color
from PIL import Image


options = {'1': '1- send clear',
           '2': '2- set color infinite duration',
           '3': '3- set color (x) duration',
           '4': '4- color gradient',
           '5': '5- send image',
           '6': '6- error request',
           '7': '7- error image',
           '8': '8- error of priority',
           '0': '0- exit'
          }


class ConnectionData():
    def __init__(self):
        self.hyperion_ip = "127.0.0.1"
        self.hyperion_ip = "192.168.1.2"
        self.hyperion_flatbuffers_port = 19400


def exec_example(hyperion, option):
    if option == 1:
        hyperion.create_clear(-1)

    elif option == 2:
        hyperion.create_clear(-1)
        hyperion.create_color(0x00AAAA00, -1)

    elif option == 3:
        hyperion.create_color(0x00880000, 2000)

    elif option == 4:
        amount = 100
        init_color = Color("#D0CA12")
        colors = list(init_color.range_to(Color("#12A3C1"),amount))

        for col in colors:
            col = col.hex[1:]
            col = int(col, 16)
            hyperion.create_color(col, -1)
            time.sleep(0.05)

    elif option == 5:
        img_name = "image.png"

        try:
            image = Image.open(img_name)
        except:
            print ("\terror: missing", img_name)
            return

        img_width, img_height = image.size

        rawData = image.tobytes()
        
        newsize = (int(img_width/10), int(img_height/10))
        image = image.resize(newsize)
        hyperion.create_image(rawData, img_width, img_height, -1)

    elif option == 6:
        hyperion.create_request("")

    elif option == 7:
        hyperion.create_image(b'\x02\x03\x05\x07', 64, 64, -1)

    elif option == 8:
        hyperion.create_register("any name", 2)


def print_options(message):
    print ("\n----------------------")
    print ("Hyperion - flatbuffers")
    print ("----------------------")
    print (message)
    print ("Options:")

    for opt in options:
        print("\t", options[opt])


if __name__ == "__main__":
    connection = ConnectionData()

    print_options("")
    option = 1
    while (option != 0):
        
        option = input("\nPlease select an option:\n")

        if (not option.isnumeric()) or (not option in options):
            print_options("\n\t---------- wrong option ----------\n")
        else:
            option = int(option)
            
            if (option != 0):
                hyperion = Hyperion(connection)

                if (not hyperion.socket_connected):
                    print ("hyperion flatbuffers server not found on:", connection.hyperion_ip, "port:", connection.hyperion_flatbuffers_port)

                else:
                    exec_example(hyperion, option)
                    del hyperion

                    print_options("")
