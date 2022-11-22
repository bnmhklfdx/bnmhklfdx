from flask import *


app = Flask(__name__)

name = ''
login = ''
@app.route('/<int:id>', methods=['GET', 'POST'])
@app.route('/', methods=('GET', 'POST'))
def index(id=None):
    global name, login
    if request.method == 'POST':
        if request.form.get('account') == 'happybirthday' and request.form.get('pwd') == 'pxw221':
            login = 'success'
            name = 'admin'
            return render_template('Shadow.html', name=name, login=login)
        else:
            login = 'fail'
        if id ==520:
            return render_template('index.html')
        if id ==1314:
            return render_template('birthdayIndex.html')
    return render_template('hellow.html')

if __name__ == '__main__':
    app.run()