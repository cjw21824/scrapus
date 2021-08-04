from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy import Column, String
from .monsterresource import MonsterResource
from .base import Base

# Monster model class - gathers id and basic stats for each monster and associates it to the resources it drops
class Monster(Base):
    __tablename__='monster'
    #Identification fields
    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String(128),nullable=False)
    minlevel = Column(Integer,nullable=False)
    maxlevel = Column(Integer,nullable=False)
    #stats - resistances and AP/MP
    minmp = Column(Integer,nullable=False)
    maxmp = Column(Integer,nullable=False)
    minap = Column(Integer,nullable=False)
    maxap = Column(Integer,nullable=False)
    family = Column(String(128),nullable=False)
    minhp = Column(Integer,nullable=False)
    maxhp = Column(Integer,nullable=False)
    minearthres = Column(Integer,nullable=False)
    maxearthres = Column(Integer,nullable=False)
    minwaterres = Column(Integer,nullable=False)
    maxwaterres = Column(Integer,nullable=False)
    minfireres = Column(Integer,nullable=False)
    maxfireres = Column(Integer,nullable=False)
    minairres = Column(Integer,nullable=False)
    maxairres = Column(Integer,nullable=False)
    minneutralres = Column(Integer,nullable=False)
    maxneutralres = Column(Integer,nullable=False)
    #relationship - resources the monster drops
    resources = relationship("MonsterResource", back_populates="monster")    