from .. import db


class URLDB(db.Model):
    __tablename__ = 'url_db'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    url = db.Column(db.String(1024))

    @staticmethod
    def add(url):
        item = URLDB(url=url)
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def query(id):
        item = db.session.query(URLDB).filter_by(id=id).first()
        return item
