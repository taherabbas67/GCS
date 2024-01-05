from dronekit import connect

# Set the baud rate
baud_rate = 57600  # Replace with the baud rate of your Pixhawk

# Set your custom timeout in seconds
custom_timeout = 90  # For example, 60 seconds

# Connect to the Vehicle
print("Connecting to vehicle...")
vehicle = connect('/dev/tty.usbserial-0001', wait_ready=True, baud=baud_rate, timeout=custom_timeout)  # Ensure you replace '/dev/ttyUSB0' with your port


# "/dev/tty.usbserial-0001" for radio telemetry
# "/dev/tty.usbmodem14201" for usb wire

# Connection success message
print("Connected to vehicle.")

# Close vehicle object
vehicle.close()
