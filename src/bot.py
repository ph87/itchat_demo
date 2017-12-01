#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

import os
import itchat
import logging

from itchat.content import (
    TEXT, MAP, CARD, NOTE, SHARING,
    PICTURE, RECORDING, VOICE, ATTACHMENT,
    VIDEO, FRIENDS, SYSTEM
)

from db import insert_db

logger = logging.getLogger('itchat')


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    insert_db(msg.type, msg.text, msg.CreateTime, msg.User.NickName)
    logger.info('{}, {}, {}, {}'.format(msg.type, msg.text, msg.CreateTime,
                                        msg.User.NickName))


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    file_path = os.path.join('media', msg.fileName)
    with open(file_path, 'wb') as f:
        f.write(msg.download())
        insert_db(msg.type, msg.fileName, msg.CreateTime, msg.User.NickName)
    logger.info('{}, {}, {}, {}'.format(msg.type, msg.filename, msg.CreateTime,
                                        msg.User.NickName))


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))


itchat.auto_login(True)
itchat.run(True)
