from market import app
from flask import render_template,redirect,url_for
from market.models import Item
from market.forms import RegisterForm

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
def market_page():
    items = [
        {"id": 1, "name": "Phone", "barcode": 123456789, "price": 500},
        {"id": 2, "name": "Laptop", "barcode": 123654789, "price": 500},
        {"id": 3, "name": "keybord", "barcode": 123456987, "price": 150},
    ]
    items = Item.query.all()
    return render_template("market.html", items=items)

@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        # 创建用户
        print("用户{username}创建成功".format(username=form.username.data))
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            print(err_msg)
    return render_template("register.html", form=form)