#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from datetime import datetime

from sqlalchemy import (
    create_engine, MetaData, Table, Column, Text, String,
    ForeignKey, Integer, DateTime
)

engine = create_engine('sqlite:///sqlite.db', echo=True)
metadata = MetaData(engine)

message_table = Table(
    'message_table', metadata,
    Column('id', Integer, primary_key=True),
    Column('message', Text),
    Column('message_type', String(10)),
    Column('message_created', String(10)),
    Column('user_nickname', String(100)),
    Column('dt_created', DateTime())
)

message_table.create(checkfirst=True)

conn = engine.connect()

def insert_db(message_type, message, create_time, nickname):
    ins = message_table.insert()
    ins = ins.values(message_type=message_type, message=message,
                     message_created=create_time, user_nickname=nickname,
                     dt_created=datetime.now(),)
    result = conn.execute(ins)
    return result
