window.onload = function () {
    const taskList = document.getElementById("studentTasks");
  
    const tasks = JSON.parse(localStorage.getItem("tasks") || "[]");
    const quizzes = JSON.parse(localStorage.getItem("quizzes") || "[]");
    const notes = JSON.parse(localStorage.getItem("notes") || "[]");
  
    // Display Tasks
    if (tasks.length > 0) {
      const taskTitle = document.createElement("h3");
      taskTitle.textContent = "📝 Assigned Tasks";
      taskList.appendChild(taskTitle);
  
      tasks.forEach(task => {
        const li = document.createElement("li");
        li.innerHTML = `<strong>${task.title}</strong><br>${task.description}<br><em>Assigned to: ${task.student}</em>`;
        taskList.appendChild(li);
      });
    }
  
    // Display Quizzes
    if (quizzes.length > 0) {
      const quizTitle = document.createElement("h3");
      quizTitle.textContent = "📚 Quizzes";
      taskList.appendChild(quizTitle);
  
      quizzes.forEach(quiz => {
        const li = document.createElement("li");
        li.innerHTML = `<strong>${quiz.title}</strong><br>
          <b>Q:</b> ${quiz.question}<br>
          <b>Options:</b> ${quiz.options.join(", ")}<br>
          <em>Assigned to: ${quiz.student}</em>`;
        taskList.appendChild(li);
      });
    }
  
    // Display Notes
    if (notes.length > 0) {
      const noteTitle = document.createElement("h3");
      noteTitle.textContent = "📄 Notes";
      taskList.appendChild(noteTitle);
  
      notes.forEach(note => {
        const li = document.createElement("li");
        li.innerHTML = `<strong>${note.title}</strong><br>${note.content}<br><em>Uploaded by: ${note.teacher}</em>`;
        taskList.appendChild(li);
      });
    }
  };
  