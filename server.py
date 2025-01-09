from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')  # Załaduj stronę HTML

@app.route('/ring', methods=['POST'])
def ring():
    # Emitowanie zdarzenia WebSocket do wszystkich połączonych klientów
    socketio.emit('play_sound')
    return 'Dźwięk wysłany', 200

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)  # Uruchomienie serwera Flask
