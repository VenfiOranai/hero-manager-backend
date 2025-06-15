from flask_socketio import SocketIO
from src.factory import create_app
from src.socketio import socketio_app

if __name__ == '__main__':
    app = create_app()
    socketio_app.init_app(app)
    socketio_app.run(app, debug=True, host='0.0.0.0', port=8080, allow_unsafe_werkzeug=True)
