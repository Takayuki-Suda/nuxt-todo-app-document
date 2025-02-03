from flask import Flask, render_template, send_from_directory
from functools import partial

app = Flask(__name__, static_folder='static', template_folder='html')

@app.route('/')
def home():
    return send_from_directory('html/home', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('html', path)

def render_task_management(template_path, filename):
    return render_template(f'{template_path}/task-management/{filename}')

# 動的にルートを生成
task_management_routes = [
    'detailed-design',
    'requirements_and_design',
    'technology-details'
]

for route in task_management_routes:
    app.add_url_rule(
        f'/{route}/task-management/<filename>',
        endpoint=f'task_management_{route.replace("-", "_")}', 
        view_func=partial(render_task_management, route)
    )

if __name__ == '__main__':
    app.run(debug=True)
