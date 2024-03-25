from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# 配置数据库
# 'sqlite:///market.sqlite'
DB_URI = 'sqlite:///market.sqlite'
# DB_URI = 'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8'.format(
#     USERNAME=USERNAME,
#     PASSWORD=PASSWORD,
#     HOST=HOST,
#     PORT=PORT,
#     DATABASE=DATABASE
# )
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '08828e2a1c6e1e35cf020c09'
app.static_folder = 'static'

db = SQLAlchemy()
migrate = Migrate()

# 初始化插件
db.init_app(app)
migrate.init_app(app, db)

from market import routes
