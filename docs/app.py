from flask import Flask, render_template, send_from_directory
from functools import partial

app = Flask(__name__, static_folder='static', template_folder='html')

@app.route('/')
def home():
    return send_from_directory('html/home', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('html', path)

# 共通のレンダリング関数
def render_dynamic_template(base_path, template_path, filename):
    return render_template(f'{base_path}/{template_path}/{filename}')

# 動的にルートを生成する共通関数
def add_dynamic_routes(routes, base_paths, view_func):
    """動的ルートを追加する共通処理"""
    for base_path in base_paths:
        for route in routes:
            app.add_url_rule(
                f'/{route}/{base_path}/<filename>',
                endpoint=f'{base_path}_{route.replace("/", "_").replace("-", "_")}',
                view_func=partial(view_func, route, base_path)
            )

# ルートの定義
task_management_routes = [
    'detailed-design',
    'requirements_and_design',
    'technology-details',
    'home'
]

# base_pathのリスト
base_paths = [
    'task-management',
    'featureA',
    ''
]

# 動的にルートを追加
add_dynamic_routes(task_management_routes, base_paths, render_dynamic_template)

if __name__ == '__main__':
    app.run(debug=True)
