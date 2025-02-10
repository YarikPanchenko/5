from flask import Flask, render_template, make_response
import os, random

app = Flask(__name__)

@app.route('/')
def index():
    file_path = 'data/info.txt'  # Путь к файлу
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            messages = file.read()  # Читаем содержимое файла
    else:
        messages = "Файл не найден!"

    # Отключаем кэширование
    response = make_response(render_template('tempindex.html', messages=messages))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

if __name__ == '__main__':
    app.run(debug=True)
