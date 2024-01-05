# dependencies
from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket
# import exceptions
import math
# import argparser
import argparse


# functions
def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()

    connection_string = args.connect

    vehicle = connect('/dev/tty.URT0', wait_ready=True)

    return vehicle

# main
vehicle = connectMyCopter()