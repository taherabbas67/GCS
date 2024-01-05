from dronekit import connect

# Connect to the Vehicle
print("Connecting to vehicle...")
vehicle = connect('/dev/tty.URT0', wait_ready=True)  # Replace '/dev/ttyUSB0' with the appropriate USB port

# Print a message upon successful connection
print("Connection successful!")

# Close vehicle object
vehicle.close()
