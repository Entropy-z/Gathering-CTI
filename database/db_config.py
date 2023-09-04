from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("URL_DB")
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Ransomware(Base):
    __tablename__ = 'ransomware'
    
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    victim = Column(String)
    group = Column(String)

class Phishing(Base):
    __tablename__ = 'phishing'
    
    id = Column(Integer, primary_key=True)
    url = Column(String)
    id_phishing= Column(String)
    submitted_by = Column(String)

class CVEs(Base):
    __tablename__ = 'cves'
    
    id = Column(Integer, primary_key=True)
    cve = Column(String)
    published = Column(DateTime)
    description = Column(String)

def inserir_dados_no_banco(funcao):
    data = funcao()  

    for item in data:
        cve_entry = CVEs(cve=item['cve'], published=item['published'], description=item['description'])
        session.add(cve_entry)

    session.commit()    