from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy_utils import create_database, database_exists

DB_USER = "postgres"
DB_PASSWORD = "123"
DB_NAME = "test"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}",
    echo=True,
)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Album(Base): 
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist_id = Column(Integer, ForeignKey('artist.id'), nullable=False)
    artist = relationship("Artist", backref="albums")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
artist = Artist(name="MyBand")
album = Album(name="MyAlbum", artist=artist)
session.add_all([artist, album])
session.commit()
