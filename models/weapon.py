from sqlalchemy.dialects.postgresql import INT4RANGE
from sqlalchemy.types import Integer, String, Text, Boolean
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from models.base import Base

# Weapon model class - gathers id, type,level, etc. Gathers all the basic stats for each weapon. Does not currently gather incarnations and other special effects.
class Weapon(Base):
    __tablename__ = 'weapon'
    #identification
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=False)
    type = Column(String, nullable = False)
    level = Column(Integer, nullable = False)
    name = Column(String, nullable = False)
    description = Column(Text, nullable = True)
    #characteristics
    ap_cost = Column(Integer, nullable=False)
    crit_hit_chance = Column(Integer, nullable = False)
    crit_hit_bonus = Column(Integer, nullable = True)
    conditions = Column(Text, nullable = True)
    #Core Effects
    effective_range = Column(INT4RANGE, nullable=True)
    percent_air_res= Column(INT4RANGE, nullable = True)
    percent_earth_res= Column(INT4RANGE, nullable = True)
    percent_fire_res= Column(INT4RANGE, nullable = True)   
    percent_neutral_res= Column(INT4RANGE, nullable = True)
    percent_water_res= Column(INT4RANGE, nullable = True)
    percent_ranged_res= Column(INT4RANGE, nullable= True)
    percent_weapon_damage= Column(INT4RANGE, nullable = True)
    percent_ranged_damage= Column(INT4RANGE, nullable = True)
    percent_spell_damage= Column(INT4RANGE, nullable = True)
    percent_crit= Column(INT4RANGE, nullable = True)
    crit_damage= Column(INT4RANGE, nullable = True)
    crit_res= Column(INT4RANGE, nullable = True)
    vitality= Column(INT4RANGE, nullable = True)
    agility= Column(INT4RANGE, nullable = True)
    air_damage= Column(INT4RANGE, nullable = True)
    air_res= Column(INT4RANGE, nullable = True)
    strength= Column(INT4RANGE, nullable = True)
    earth_damage= Column(INT4RANGE, nullable = True)
    earth_Res= Column(INT4RANGE, nullable = True)
    intelligence= Column(INT4RANGE, nullable = True)
    fire_damage= Column(INT4RANGE, nullable = True)
    fire_res= Column(INT4RANGE, nullable = True)
    wisdom= Column(INT4RANGE, nullable = True)
    neutral_damage= Column(INT4RANGE, nullable = True)
    neutral_res= Column(INT4RANGE, nullable = True)
    chance= Column(INT4RANGE, nullable = True)
    water_damage= Column(INT4RANGE, nullable = True)
    water_Res= Column(INT4RANGE, nullable = True)
    damage= Column(INT4RANGE, nullable = True)
    ap= Column(INT4RANGE, nullable = True)
    ap_parry= Column(INT4RANGE, nullable = True)
    ap_reduction= Column(INT4RANGE, nullable = True)
    mp= Column(INT4RANGE, nullable = True)
    mp_parry= Column(INT4RANGE, nullable = True)
    mp_reduction= Column(INT4RANGE, nullable = True)
    dodge= Column(INT4RANGE, nullable = True)
    heals= Column(INT4RANGE, nullable = True)
    initiative= Column(INT4RANGE, nullable = True)
    lock= Column(INT4RANGE, nullable = True)
    range= Column(INT4RANGE, nullable = True)
    prospecting= Column(INT4RANGE, nullable = True)
    pushback_damage= Column(INT4RANGE, nullable = True)
    pushback_res= Column(INT4RANGE, nullable = True)
    power = Column(INT4RANGE, nullable = True)
    trap_power= Column(INT4RANGE, nullable = True)
    trap_damage= Column(INT4RANGE, nullable = True)
    steals_kamas= Column(INT4RANGE, nullable = True)
    attack_neutral_damage=Column(INT4RANGE, nullable = True)
    attack_fire_damage=Column(INT4RANGE, nullable = True)
    attack_water_damage=Column(INT4RANGE, nullable = True)
    attack_earth_damage=Column(INT4RANGE, nullable = True)
    attack_air_damage=Column(INT4RANGE, nullable = True)
    attack_neutral_steal=Column(INT4RANGE, nullable = True)
    attack_fire_steal=Column(INT4RANGE, nullable = True)
    attack_water_steal=Column(INT4RANGE, nullable = True)
    attack_earth_steal=Column(INT4RANGE, nullable = True)
    attack_air_steal=Column(INT4RANGE, nullable = True)
    attack_hp_steal=Column(INT4RANGE, nullable=True)
    summons = Column(INT4RANGE, nullable = True)    
    is_hunting_weapon = Column(Boolean, nullable = True)
    use_per_turn = Column(Integer, nullable = True)
    #Relationships
    recipe = relationship('Recipe', back_populates='weapon', uselist=False)
    ingredients = relationship('Ingredient', back_populates='weapon')