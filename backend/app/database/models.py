from .database import db

#Laundry Store Model
class LaundryStore(db.Model):
    __tablename__ = 'laundry store'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    last_updated = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(50), nullable=True)
    free_delivery = db.Column(db.Boolean, default=False)

    #Relationships
    address = db.relationship('Address', backref = 'laundry_store', uselist = False) #One to one
    hours = db.relationship('Hours', backref = 'laundry_store', uselist=False, lazy='joined') #One to One | Joined loading - loads same time as parent (laundry store)
    wash_and_fold_price = db.relationship('WashAndFoldPrice', backref='laundry_store', uselist=False) #One to one
    dry_cleaning_price = db.relationship('DryCleaningPrice', backref='laundry_store', uselist=False) #One to one
    reviews = db.relationship('Reviews', backref='laundry_store', lazy='dynamic') #One to many | lazy dynamic - returns query object rather then all results at once

#Address Model
class Address(db.Model):
    __tablename__ = 'address'

    laundry_id = db.Column(db.Integer, db.ForeignKey('laundry_store.id'), primary_key=True)
    address_1 = db.Column(db.String(50), nullable=False)
    address_2 = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.integer, nullable=False)

#Hours Model
class Hours(db.Model):
    __tablename__ = 'hours'

    laundry_id = db.Column(db.Integer, db.ForeignKey('laundry_store.id'), primary_key=True)
    mon = db.Column(db.String(50), nullable=False)
    tue = db.Column(db.String(50), nullable=False)
    wed = db.Column(db.String(50), nullable=False)
    thur = db.Column(db.String(50), nullable=False)
    fri = db.Column(db.String(50), nullable=False)
    sat = db.Column(db.String(50), nullable=False)
    sun = db.Column(db.String(50), nullable=False)

#Reviews Model
class Reviews(db.Model):
    __tablename__ = 'reviews'

    laundry_id = db.Column(db.Integer, db.ForeignKey('laundry_store.id'), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    review = db.Column(db.String(100), nullable=False)

#Wash and Fold Price Model
class WashAndFoldPrice(db.Model):
    __tablename__ = 'wash_and_fold_price'

    laundry_id = db.Column(db.Integer, db.ForeignKey('laundry_store.id'), primary_key=True)
    min_price = db.Column(db.Numeric, nullable=True)
    min_pounds = db.Column(db.Numeric, nullable=True)
    price_per_pound = db.Column(db.Numeric, nullable=False)

#Dry Cleaning Price Model
class DryCleaningPrice(db.Model):
    __tablename__ = 'dry_cleaning_price'

    laundry_id = db.Column(db.Integer, db.ForeignKey('laundry_store.id'), primary_key=True)
    dress = db.Column(db.Numeric, nullable=True)
    sweater = db.Column(db.Numeric, nullable=True)
    skirt = db.Column(db.Numeric, nullable=True)
    shorts = db.Column(db.Numeric, nullable=True)
    outer_jacket = db.Column(db.Numeric, nullable=True)
    coat = db.Column(db.Numeric, nullable=True)
    jump_suit = db.Column(db.Numeric, nullable=True)
    launder_shirt = db.Column(db.Numeric, nullable=True)
    dry_clean_shirt = db.Column(db.Numeric, nullable=True)
    blouse = db.Column(db.Numeric, nullable=True)
    pants = db.Column(db.Numeric, nullable=True)
    suit_jacket = db.Column(db.Numeric, nullable=True)
    two_piece_suit = db.Column(db.Numeric, nullable=True)
    robe = db.Column(db.Numeric, nullable=True)
    scarf = db.Column(db.Numeric, nullable=True)
    tie = db.Column(db.Numeric, nullable=True)
    tuxedo = db.Column(db.Numeric, nullable=True)
    three_piece_suit = db.Column(db.Numeric, nullable=True)