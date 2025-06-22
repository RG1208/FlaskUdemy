from .extensions import db  # type: ignore

class MyModel(db.Model):
    __tablename__ = 'my_model'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<MyModel {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }