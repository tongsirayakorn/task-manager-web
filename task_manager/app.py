from flask import Flask, request, redirect, render_template

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task = request.form.get('task')
        deadline = request.form.get('deadline')
        print("TASK =", task)
        print("DEADLINE =", deadline)
        if task:
            tasks.append({
               "text": task,
               "done": False,
               "deadline": deadline
        })
    return render_template('index.html', tasks=list(enumerate(tasks)))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect('/')

@app.route('/toggle/<int:index>')
def toggle(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index]["done"]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)