from sqlalchemy import Column
from sqlalchemy.orm import relationship
from models.recipe import Recipe
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.types import String, Text
from models.base import Base

#Profession Model class - Adds each profession's id, name, and description. Associates recipes that each profession can make
class Profession(Base):
    __tablename__ = 'profession'
    #identification fields
    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String,nullable = False)
    description = Column(Text, nullable=True)
    #relationship
    recipes = relationship("Recipe")