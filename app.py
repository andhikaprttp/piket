from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'secret_key' 

# Daftar siswa
students = []

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    students.append(name)
    flash('Siswa berhasil ditambahkan', 'success')
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    name = request.form.get('name')
    if name in students:
        students.remove(name)
        flash('Siswa berhasil dihapus', 'success')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)