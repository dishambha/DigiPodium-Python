from email.policy import default
from enum import unique
from turtle import title
import streamlit as st
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
#create a model class
Base = declarative_base()         #boilerplate code

class Food(Base):
    __tablename__ = 'food_table'
    id = Column(Integer, primary_key=True)
    title = Column(String(100),unique= True)
    duration = Column(Integer, default = 2)
    ingredients = Column(String)
    category = Column(String, default="veg")
    kind = Column(String(50), default='south-indiam')
    created_on = Column(Date, default=datetime.now())

    def __str__(self):
        return f'{self.title}({self.kind})'

#create a data base
engine = create_engine('sqlite://food.sqlite', echo=True)   #blank database
Base.metadata.create_all(engine)                            #create all the table

#open the database ->also boilerplate code
def open_db():
    Session = sessionmaker(bind=engine)
    return Session()

#save data in db
def save_food(title, duration=2, ingredients="", category="veg", kind="south-indian" ):
    db = open_db()
    food = Food(title=title, duration= duration, ingredients= ingredients, category,kind=kind)
    db.add(food)   #add obj to the db
    db.commit()    #save the data
    db.close       #close the connection

def load_all_food():
    db =  open_db()
    foods = db.query(Food).all()       #get all the data
    db.close()
    return foods

def delete_food(id):
    db = open_db()
    try:
        db.query(Food).filter(Food.id == id).delete()  #delete the data
        db.commit()
    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        db.close

#ui using streamlit

st.title("Food CRUD App")
with st.form("form"):
    title = st.text_input("Title")
    duration = st.number_input("Duration in minutes", min_value=2, max_value=24*60)
    ingredients = st.text_area("")
        