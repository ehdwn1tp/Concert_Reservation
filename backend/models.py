from sqlalchemy import Column, Integer, String, SmallInteger, DateTime, ForeignKey
from sqlalchemy.types import PickleType
from sqlalchemy.orm import relationship

from database import Base

class Play(Base):
    __tablename__ = "Play"

    id = Column('ID', Integer, primary_key=True, autoincrement=True) # ID
    code = Column('CODE', String(2), nullable=False) # 작품 코드
    name = Column('NAME', String(5), nullable=False) # 작품 이름
    license = Column('LICENSE', SmallInteger, nullable=False) # 라이센스 유무
    type = Column('TYPE', SmallInteger, nullable=False) # 작품 종류 (0: 연극 / 1: 뮤지컬)
    update = Column('UPDATE', DateTime, nullable=False) # 수정 일자


class Performance(Base):
    __tablename__ = "Performance"

    id = Column('ID', Integer, primary_key=True, autoincrement=True) # ID
    code = Column('CODE', String(2), nullable=False) # 공연 코드
    name = Column('NAME', String, nullable=False) # 공연 이름
    play_code = Column('PLAY_CODE', String, ForeignKey(Play.code), nullable=False) # 작품 코드
    generation = Column('GENERATION', SmallInteger, nullable=False) # 공연 기수
    round = Column('ROUND', String, nullable=False) # 공연 회차
    time = Column('TIME', String, nullable=False) # 공연 시간
    thtr_id = Column('THEATER_ID', String) # 극장 코드
    actors = Column('ACTORS', String) # 배우 및 관계자 명단
    update = Column('UPDATE', DateTime) # 수정 일자


class Theater(Base):
    __tablename__ = "Theater"

    id = Column('ID', Integer, primary_key=True, autoincrement=True) # ID
    name = Column('NAME', String) # 극장 이름
    address = Column('ADDRESS', String) # 극장 주소
    price = Column('PRICE', Integer) # 대관료
    contact = Column('CONTACT', String) # 극장 연락처 (02-000-0000)
    size = Column('SIZE', SmallInteger) # 수용 가능 관객 수
    update = Column('UPDATE', DateTime) # 수정 일자


class Actor(Base):
    __tablename__ = "Actor"

    id = Column('ID', Integer, primary_key=True, autoincrement=True) # ID
    name = Column('NAME', String(5)) # 배우 이름
    contact = Column('CONTACT', String) # 배우 연락처 (02-000-0000)
    update = Column('UPDATE', DateTime) # 수정 일자


class Reservation(Base):
    __tablename__ = "Reservation"

    id = Column('ID', Integer, primary_key=True, autoincrement=True) # ID
    code = Column('CODE', String) # 공연 코드(00000000) + 예매ID(000000) : 14자리
    prf_code = Column('PRF_CODE', String, ForeignKey(Performance.code)) # 공연 코드
    name = Column('NAME', String(5)) # 예매자 이름
    license = Column('LICENSE', SmallInteger)
    type = Column('TYPE', SmallInteger)
    update = Column('UPDATE', DateTime) # 수정 일자