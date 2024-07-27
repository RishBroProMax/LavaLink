from flask import Flask, jsonify
import psutil
import time

app = Flask(__name__)

def get_uptime():
    return time.time() - psutil.boot_time()

def get_network_speed():
    return {"upload": "N/A", "download": "N/A"}

@app.route('/status')
def status():
    disk_usage = psutil.disk_usage('/')
    memory_info = psutil.virtual_memory()
    uptime = get_uptime()
    network_speed = get_network_speed()
    
    status_info = {
        "disk": {
            "total": disk_usage.total,
            "used": disk_usage.used,
            "free": disk_usage.free,
            "percent": disk_usage.percent
        },
        "memory": {
            "total": memory_info.total,
            "available": memory_info.available,
            "percent": memory_info.percent,
            "used": memory_info.used,
            "free": memory_info.free
        },
        "uptime": uptime,
        "network_speed": network_speed
    }
    
    return jsonify(status_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
