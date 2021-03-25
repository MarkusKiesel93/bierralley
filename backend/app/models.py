from sqlalchemy import Column, String, Integer

from app.database import Base, engine


def create_models():
    Base.metadata.create_all(bind=engine)


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    contact = Column(String, unique=True, index=True)
    channel = Column(String)
    first_name_player_1 = Column(String)
    last_name_player_1 = Column(String)
    drink_pref_player_1 = Column(String)
    first_name_player_2 = Column(String)
    last_name_player_2 = Column(String)
    drink_pref_player_2 = Column(String)
    time_pref = Column(String)
    registration_date = Column(String)

