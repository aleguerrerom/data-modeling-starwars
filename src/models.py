import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'Character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)

class FavoriteCharacter(Base):
    __tablename__ = 'Favorite_Character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    
    id = Column(Integer, primary_key=True)
    username_id = Column(Integer, ForeignKey('User.id'))
    character_id = Column(Integer, ForeignKey('Character.id'))

class FavoritePlanet(Base):
    __tablename__ = 'Favorite_Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    
    id = Column(Integer, primary_key=True)
    username_id = Column(Integer, ForeignKey('User.id'))
    planet_id = Column(Integer, ForeignKey('Planet.id'))

class User(Base):
    __tablename__='User'
    id = Column(Integer, primary_key=True)
    username = Column(Integer, nullable=False)
    password = Column(Integer, nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')