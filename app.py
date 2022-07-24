from flask import *

app = Flask(__name__)
app.secret_key = 'n@aiKauJ@'


@app.route('/')
def home():
    return render_template('homePage.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password and email != '' and fname != '' and lname != '':
            print(f'{fname} \n{lname} \n{email} \n{password}')
            session['fname'] = fname
            session['lname'] = lname
            session['email'] = email
            session['password'] = password
            return redirect(url_for('login'))
        else:
            error = 'Invalid credentials. Please try again.'
            flash(error)
    return redirect(url_for('home'))


@app.route('/login')
def login():
    return render_template('loginPage.html')


@app.route('/login_user', methods=['POST'])
def login_user():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == session['email'] and password == session['password']:
            print(f'{email} \n{password}')
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid Credentials. Please try again.'
            flash(error)
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    return render_template('dashBoard.html')


@app.route('/get_salary', methods=['GET', 'POST'])
def get_salary():
    error = None
    if request.method == 'POST':
        salary = request.form['salary']
        if salary != '':
            print(salary)
            if salary in range(100, 1000):
                save = salary * 0.06
                net = salary - save
                budget = net/28
                print(save)
                print(net)
                print(budget)
                return render_template('dashBoard.html', salary=salary, save=save, net=net, budget=budget)
            elif salary in range(1000, 10000):
                save = salary * 0.08
                net = salary - save
                budget = net/28
                print(save)
                print(net)
                print(budget)
                return render_template('dashBoard.html', salary=salary, save=save, net=net, budget=budget)
            elif salary in range(10000, 100000):
                save = salary * 0.1
                net = salary - save
                budget = net/28
                print(save)
                print(net)
                print(budget)
                return render_template('dashBoard.html', salary=salary, save=save, net=net, budget=budget)
            elif salary in range(100000, 1000000):
                save = salary * 0.12
                net = salary - save
                budget = net/28
                print(save)
                print(net)
                print(budget)
                return render_template('dashBoard.html', salary=salary, save=save, net=net, budget=budget)
            elif salary in range(1000000, 10000000):
                save = salary * 0.14
                net = salary - save
                budget = net/28
                print(save)
                print(net)
                print(budget)
                return render_template('dashBoard.html', salary=salary, save=save, net=net, budget=budget)
            elif salary in range(10000000, 100000000):
                save = salary * 0.16
                net = salary - save
                budget = net/28
                print(save)
                print(net)
                print(budget)
                return render_template('dashBoard.html', salary=salary, save=save, net=net, budget=budget)
            elif salary in range(100000000, 1000000000):
                save = salary * 0.18
                net = salary - save
                budget = net/28
                print(save)
                print(net)
                print(budget)
                return render_template('dashBoard.html', salary=salary, save=save, net=net, budget=budget)
            elif salary in range(1000000000, 10000000000):
                save = salary * 0.2
                net = salary - save
                budget = net/28
                print(save)
                print(net)
                print(budget)
                return render_template('dashBoard.html', salary=salary, save=save, net=net, budget=budget)
            else:
                save = salary * 0.25
                net = salary - save
                budget = net/28
                print(save)
                print(net)
                print(budget)
                return render_template('dashBoard.html', salary=salary, save=save, net=net, budget=budget)
            

        else:
            error = 'Invalid Credentials. Please try again.'
            flash(error)
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True, port=5050)
