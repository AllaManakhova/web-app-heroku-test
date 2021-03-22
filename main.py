import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от приложения Flask"


# os.environ получаем значение переменной окружения с именем PORT (по умолчанию 5000)
# host = 0.0.0.0 означает, что мы разрешаем подключения из любой сети по любому интерфейсу
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


# from flask import Flask
# from flask_ngrok import run_with_ngrok
#
# app = Flask(__name__)
# run_with_ngrok(app)
#
#
# @app.route("/")
# def index():
#     return "Привет от приложения Flask"
#
#
# if __name__ == '__main__':
#     app.run()