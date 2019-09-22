# app/models.py

from app import db

class Config(db.Model):
    """This class represents the bucketlist table."""

    __tablename__ = 'config'

    count = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.String(36))
    title = db.Column(db.String(255))
    columns = db.Column(db.JSON)
    properties = db.Column(db.JSON)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, id, title, columns, properties):
        """initialize with id."""
        self.id = id
        self.title = title
        self.columns = columns
        self.properties = properties

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Config.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Config: {}>".format(self.title)
    
    
class Workflow(db.Model):
    """This class represents the bucketlist table."""

    __tablename__ = 'workflow'
    
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    RelId = db.Column(db.String(255))
    EntityType = db.Column(db.String(255))
    DseDsCode = db.Column(db.String(255))
    OdsStatus = db.Column(db.String(255))
    GplStatus = db.Column(db.String(255))
    GblStatus = db.Column(db.String(255))
    GrlStatus = db.Column(db.String(255))
    DetStatus = db.Column(db.String(255))
    GckStatus = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, RelId, EntityType, DseDsCode, OdsStatus, GplStatus, GblStatus, GrlStatus, DetStatus, GckStatus):
        self.RelId = RelId
        self.EntityType = EntityType
        self.DseDsCode = DseDsCode
        self.OdsStatus = OdsStatus
        self.GplStatus = GplStatus
        self.GblStatus = GblStatus
        self.GrlStatus = GrlStatus
        self.DetStatus = DetStatus
        self.GckStatus = GckStatus

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Workflow.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Workflow: {}>".format(self.Id)
    
    
class Rules(db.Model):
    """This class represents the bucketlist table."""

    __tablename__ = 'rules'
    
    Name = db.Column(db.String(255), primary_key=True)
    Type = db.Column(db.String(255))
    Salary = db.Column(db.String(255))
    Age = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, Name, Type, Salary, Age):
        """initialize with RelId."""
        self.Name = Name
        self.Type = Type
        self.Salary = Salary
        self.Age = Age

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Rules.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Rules: {}>".format(self.Name)