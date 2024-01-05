from dronekit import connect

# Set the baud rate
baud_rate = 9600  # Replace with the baud rate of your Pixhawk

# Connect to the Vehicle
print("Connecting to vehicle...")
vehicle = connect('/dev/tty.URT0', wait_ready=True, baud=baud_rate)  # Ensure you replace '/dev/ttyUSB0' with your port

# Connection success message
print("Connected to vehicle.")

# Close vehicle object
vehicle.close()
