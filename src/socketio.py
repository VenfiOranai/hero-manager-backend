from flask_socketio import SocketIO

socketio_app = SocketIO(cors_allowed_origins="*")

def broadcast_hero_created(hero_dict: dict):
    socketio_app.emit("hero_created", hero_dict)
    