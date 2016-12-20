# -*- coding: utf-8 -*-
import os
from sqlalchemy import create_engine,MetaData,text
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash,make_response

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

#密钥
SECRET_KEY = 'development key'

DATABASE_URI = "mysql://root:asd123@192.168.120.4:3306/weixin?charset=utf8"
DATABASE_CONNECT_OPTIONS = {"pool_size":20, "max_overflow":10, "pool_recycle":3600, "echo":True}
#engine = create_engine("postgresql+psycopg2://myt:123456@192.168.1.107:6543/blog", pool_size=20, max_overflow=10, pool_recycle=3600,
del os