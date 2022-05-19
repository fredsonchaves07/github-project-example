from flask import Flask

app = Flask(__name__)

students = [
        {"id": 1, "name": "João", "course": "Sistemas de Informacao"},
        {"id": 2, "name": "Maria", "course": "Medicina"}
]


@app.route('/')
def hello_world():
    return 'ok'


@app.route("/students")
def list_students():
    return {
        "students": students
    }

if __name__ == '__main__':
    app.run()
