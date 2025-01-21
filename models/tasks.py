from extensions import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    date = db.Column(db.String)

    def to_dict(self):
    
        return {"title": self.title, "date": self.date} 
    
    