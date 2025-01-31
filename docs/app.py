from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static', template_folder='html')

@app.route('/')
def home():
    return send_from_directory('html/home', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('html', path)

@app.route('/detailed-design/task-management/index.html')
def detailed_design_index():
    return render_template('detailed-design/task-management/index.html')

@app.route('/detailed-design/task-management/data-model.html')
def data_model():
    return render_template('detailed-design/task-management/data-model.html')

@app.route('/detailed-design/task-management/sample-code.html')
def sample_code():
    return render_template('detailed-design/task-management/sample-code.html')


if __name__ == '__main__':
    app.run(debug=True)
