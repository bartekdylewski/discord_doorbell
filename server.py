from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

PORT = 8000
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')  # Załaduj stronę HTML

@app.route('/ring', methods=['POST'])
def ring():
    data = request.json  # Pobierz dane z żądania POST
    message = data.get('message')  # Domyślna wiadomość
    nickname = data.get('nickname', 'Gość')  # Domyślny nick

    # Emitowanie zdarzenia WebSocket do wszystkich połączonych klientów
    socketio.emit('play_sound', {'message': message, 'nickname': nickname})
    return 'Dźwięk i wiadomość wysłane', 200

if __name__ == '__main__':
    print(f"uruchamiam serwer na http://localhost:{PORT}/")
    socketio.run(app, host='0.0.0.0', port=PORT)  # Uruchomienie serwera Flask