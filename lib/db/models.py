from sqlalchemy import Column, String, Integer, Table, ForeignKey, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FileSystem(Base):
    __tablename__ = 'file_system'

    id = Column(Integer(), primary_key=True)
    location = Column('location', String())
    file_name = Column('file_name', String())
    file_size= Column('file_size', Integer())
    file_type= Column('file_type', String())
    file_ownership= Column('file_ownership', String())

    def __repr__(self):
        return f'''
            location: {self.location},
            file_name: {self.file_name},
            file_size: {self.file_size},
            file_type: {self.file_type},
            file_ownership: {self.file_ownership}
        '''

class FileStructure(Base):
    __tablename__ = 'file_structure'

    id = Column(Integer(), primary_key=True)
    current_directory = Column('current_directory', String())
    parent_directory = Column('parent_directory', String())

    def __repr__(self):
        return f'''
            current_directory: {self.current_directory},
            parent_directory: {self.parent_directory}
        '''
