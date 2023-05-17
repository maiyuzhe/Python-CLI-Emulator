from sqlalchemy import Column, String, Integer, Table, ForeignKey, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FileSystem(Base):
    __tablename__ = 'file_system'

    id = Column(Integer(), primary_key=True)
    location = Column('location', String())
    file_name = Column('file_name', String())
    file_size= Column('file_size', Integer())

    def __repr__(self):
        return f'''
            location: {self.location},
            file_name: {self.file_name},
            file_size: {self.file_size}
        '''
