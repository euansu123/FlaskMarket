from market import db
class Item(db.Model):
    # 表名
    __tablename__ = 'tb_item'
    # 表字段
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30),nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=True)
    barcode = db.Column(db.String(length=12), nullable=True, unique=True)
    description = db.Column(db.String(length=1024), nullable=True, unique=True)