from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy teacher credentials
teachers = {
    "monisha": "123",
    "teacher1": "pass123",
    "admin": "admin"
}

# Simulated in-memory storage
data = {
    "tasks": [],
    "quizzes": [],
    "notes": [],
    "submissions": []
}

@app.route("/")
def home():
    return "Classroom Manager Backend is running!"

# Teacher login endpoint
@app.route("/login", methods=["POST"])
def login():
    creds = request.get_json()
    username = creds.get("username")
    password = creds.get("password")
    if teachers.get(username) == password:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False}), 401

# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(data["tasks"])

# Create task
@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.get_json()
    data["tasks"].append(task)
    return jsonify({"message": "Task added."}), 201

# Get all quizzes
@app.route("/quizzes", methods=["GET"])
def get_quizzes():
    return jsonify(data["quizzes"])

# Create quiz
@app.route("/quizzes", methods=["POST"])
def add_quiz():
    quiz = request.get_json()
    data["quizzes"].append(quiz)
    return jsonify({"message": "Quiz added."}), 201

# Get notes
@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(data["notes"])

# Upload note
@app.route("/notes", methods=["POST"])
def upload_note():
    note = request.get_json()
    data["notes"].append(note)
    return jsonify({"message": "Note uploaded."}), 201

# Get submissions
@app.route("/submissions", methods=["GET"])
def get_submissions():
    return jsonify(data["submissions"])

# Add submission (quiz or task)
@app.route("/submissions", methods=["POST"])
def submit():
    submission = request.get_json()
    data["submissions"].append(submission)
    return jsonify({"message": "Submission saved."}), 201

if __name__ == "__main__":
    app.run(debug=True)
