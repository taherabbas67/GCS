from dronekit import connect, VehicleMode
import time

# Function to check if the vehicle is still connected
def is_vehicle_connected(vehicle):
    try:
        # Try getting a simple property
        vehicle.mode
        return True
    except:
        return False

# Connect to the Vehicle
print("Connecting to vehicle on: '/dev/tty.usbmodem14201'")
vehicle = connect('/dev/tty.usbmodem14201', wait_ready=True)

# Keep running until manually stopped
while is_vehicle_connected(vehicle):
    # Get some vehicle attribute values and print them
    print("GPS: %s" % vehicle.gps_0)
    print("Battery: %s" % vehicle.battery)
    print("Last Heartbeat: %s" % vehicle.last_heartbeat)
    print("Is Armable?: %s" % vehicle.is_armable)
    print("System status: %s" % vehicle.system_status.state)
    print("Mode: %s" % vehicle.mode.name)  # settable

    # Wait for a short period of time before checking again
    time.sleep(1)

# Close vehicle object when the loop is exited
vehicle.close()
print("Disconnected from vehicle.")
