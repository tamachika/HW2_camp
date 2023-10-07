from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello,World"

@app.route("/goodbye")
def goodbye():
    return "Good bye!"


if __name__ == "__main__":
    # 使用するポートを明示
    app.run(port=8000)