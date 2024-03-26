from market import app
from flask import render_template,redirect,url_for,flash
from market.models import Item,User
from market.forms import RegisterForm,LoginForm
from market import db
from flask_login import login_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home_page():
    items = [
        {"id": 1, "name": "Phone", "barcode": 123456789, "price": 500},
        {"id": 2, "name": "Laptop", "barcode": 123654789, "price": 500},
        {"id": 3, "name": "keybord", "barcode": 123456987, "price": 150},
    ]
    return render_template("home.html", items=items)


@app.route("/market")
@login_required
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)

@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        # 创建用户
        user_to_create = User(username=form.username.data,
                              email_address=form.email.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        print("用户{username}创建成功".format(username=form.username.data))
        return redirect(url_for('login_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            print("{}".format(err_msg))
            flash(f"There was an error with creating account:{err_msg}", category="danger")
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))