# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import scoped_session, sessionmaker
from . import app

engine = create_engine(app.config['DATABASE_URI'], **app.config['DATABASE_CONNECT_OPTIONS'])
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))