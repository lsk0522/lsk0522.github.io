from flask import Flask
from routes import setup_routes
import detector
import motor_esp32
import motor_arduino

app = Flask(__name__)

setup_routes(app)

detector.start()
motor_esp32.start()   # ESP32 연결 (포트 자동 감지)
motor_arduino.start() # Arduino 연결 (포트 자동 감지, device_type이 arduino일 때만 활성화)

app.run(
    host='0.0.0.0',
    port=5000,
    debug=False,
    threaded=True
)