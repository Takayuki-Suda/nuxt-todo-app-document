from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return send_from_directory('html/home', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('html', path)

if __name__ == '__main__':
    app.run(debug=True)
