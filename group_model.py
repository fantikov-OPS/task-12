from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, Session
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

class Booklet(Base):
    __tablename__ = 'booklet'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    album_id = Column(Integer, ForeignKey('album.id'), nullable=False)
    album = relationship('Album', foreign_keys='Booklet.album_id', backref='booklet')


association_table = Table('associatio', Base.metadata,
                          Column('album_id', Integer, ForeignKey('album.id')),
                          Column('track_id', Integer, ForeignKey('track.id'))
                        )

class Track(Base):
    __tablename__ = 'track'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    duration = Column(Float)
    albums = relationship('Album', secondary=association_table, backref='tracks')

Base.metadata.create_all(engine)

#booklet = [Booklet(description = 'blablabal', album_id = 1)]

#with Session(engine) as session:
#    session.add_all(booklet)
#    session.commit()

#Session = sessionmaker(bind=engine)
#session = Session()
#artist = Artist(name="MyBand")
#album = Album(name="MyAlbum", artist=artist)
#session.add_all([artist, album])
#session.commit()
