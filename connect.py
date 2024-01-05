from dronekit import connect, VehicleMode
import time

# Connect to the Vehicle
print("Connecting to vehicle on: 'your USB port'")
vehicle = connect('/dev/tty.URT0', wait_ready=True)  # Change '/dev/ttyUSB0' to the appropriate USB port that is /dev/tty.URT0 in this device

# Get some vehicle attributes (state)
print("Get some vehicle attribute values:")
print(" GPS: %s" % vehicle.gps_0)
print(" Battery: %s" % vehicle.battery)
print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
print(" Is Armable?: %s" % vehicle.is_armable)
print(" System status: %s" % vehicle.system_status.state)
print(" Mode: %s" % vehicle.mode.name)    # settable

# Close vehicle object
vehicle.close()
