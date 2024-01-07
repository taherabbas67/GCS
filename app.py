from flask import Flask, jsonify
from dronekit import connect, VehicleMode
import time

app = Flask(__name__)

@app.route('/vehicle-data', methods=['GET'])
def get_vehicle_data():
    vehicle = connect('/dev/tty.usbmodem14201', wait_ready=True)
    vehicle_data = {
        "GPS": str(vehicle.gps_0),
        "Battery": str(vehicle.battery),
        "Last Heartbeat": str(vehicle.last_heartbeat),
        "Is Armable": vehicle.is_armable,
        "System Status": vehicle.system_status.state,
        "Mode": vehicle.mode.name
    }
    vehicle.close()
    return jsonify(vehicle_data)

if __name__ == '__main__':
    app.run(debug=True)
