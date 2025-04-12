from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Dummy teacher credentials
teachers = {
    "monisha": "123",
    "teacher1": "pass123",
    "admin": "admin",
    "manasa": "456",
    "bhuvana": "789"
}

# Simulated in-memory storage
data = {
    "assign": [],
    "logint": [],
    "logins": [],
    "drashbord": [],
    "notes": [],
    "students": [],
    "tasks": [],
    "quizzes": [],
    "submissions": [],
    "student": []
}

@app.route("/")
def home():
    return "backend is working successfully"

# Teacher login endpoint
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teachers WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False}), 401


# Get all tasks
@app.route("/assign", methods=["GET"])
def get_tasks():
    return jsonify(data["tasks"])

# Create task
@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.get_json()
    data["tasks"].append(task)
    return jsonify({"message": "Task added."}), 201

# Get all quizzes
@app.route("/q", methods=["GET"])
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

# Get submission
@app.route("/student", methods=["GET"])
def get_submissions():
    return jsonify(data["student"])

# Add submission (quiz or task)
@app.route("/submissions", methods=["POST"])
def submit():
    submission = request.get_json()
    data["submissions"].append(submission)
    return jsonify({"message": "Submission saved."}), 201

# Removed the incorrect route /text

if __name__ == "__main__":
    app.run(debug=True)
