from flask import Flask, render_template, redirect, request, make_response, session, abort
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

import datetime
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departments import Departments
from forms.login import LoginForm
from forms.jobs import JobsForm

from forms.user import RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        jobs = db_sess.query(Jobs).filter(
            (Jobs.user == current_user) | (Jobs.is_finished != True))
    else:
        jobs = db_sess.query(Jobs).filter(Jobs.is_finished != True)
    return make_response(render_template("index.html", jobs=jobs))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/jobs',  methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = Jobs()
        jobs.team_leader = form.team_leader.data
        jobs.job = form.job.data
        jobs.work_size = form.work_size.data
        jobs.collaborators = form.collaborators.data
        jobs.is_finished = form.is_finished.data
        current_user.jobs.append(jobs)
        db_sess.merge(current_user)  # Изменение текущего пользователя
        db_sess.commit()
        return redirect('/')
    return render_template('jobs.html', title='Добавление работы',
                           form=form)


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id, (Jobs.user == current_user | current_user.id == 1)).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id, (Jobs.user == current_user | current_user.id == 1)).first()
        if jobs:
            form.team_leader.data = jobs.team_leader
            form.job.data = jobs.job
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.is_finished.data = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id, (Jobs.user == current_user | current_user.id == 1)).first()
        if jobs:
            jobs.team_leader = form.team_leader.data
            jobs.job = form.job.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html',
                           title='Редактирование работы',
                           form=form
                           )


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    db_session.global_init("db/mars_explorer.db")

    app.run()

    # session = db_session.create_session()
    #
    # dep = Departments()
    # dep.title = "Исследование звёзд"
    # dep.chief = 1
    # dep.members = "1, 2, 3"
    # dep.email = "the_one@dep.ru"
    #
    # session.add(dep)
    # session.commit()
    #
    #
    # session = db_session.create_session()
    #
    # user = User()
    # user.surname = "Scott"
    # user.name = "Ridley"
    # user.age = 21
    # user.position = "captain"
    # user.speciality = "research engineer"
    # user.address = "module_1"
    # user.email = "scott_chief@mars.org"
    # user.hashed_password = "cap"
    #
    # session.add(user)
    # session.commit()
    #
    # job = Jobs()
    # job.team_leader = 1
    # job.job = 'deployment of residential modules 1 and 2'
    # job.work_size = 15
    # job.collaborators = '2, 3'
    # job.is_finished = False
    #
    # session.add(job)
    # session.commit()
    #
    # user = User()
    # user.surname = "Sovenish"
    # user.name = "James"
    # user.age = 35
    # user.position = "navigator"
    # user.speciality = "universe researcher"
    # user.address = "module_2"
    # user.email = "james_navi@mars.org"
    # user.hashed_password = "nav"
    #
    # session.add(user)
    # session.commit()
    #
    # user = User()
    # user.surname = "Kazinski"
    # user.name = "Rachel"
    # user.age = 23
    # user.position = "doctor"
    # user.speciality = "nurse, surgeon, psychologist"
    # user.address = "module_3"
    # user.email = "rache_healer@mars.org"
    # user.hashed_password = "doc"
    #
    # session.add(user)
    # session.commit()
    #
    # user = User()
    # user.surname = "Gishzen"
    # user.name = "Red"
    # user.age = 28
    # user.position = "mechanic"
    # user.speciality = "hand engineer"
    # user.address = "module_4"
    # user.email = "red_crafty@mars.org"
    # user.hashed_password = "mech"
    #
    # session.add(user)
    # session.commit()


if __name__ == '__main__':
    main()
