#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import itchat
from tuling.tuling import get_response
from contentHelper.Helper import *
from collector.infoCollector import *


# @itchat.msg_register('Text')
# def text_reply(msg):
#     code = msg['Text']
#     data = getLatestInfo(code)
#     if data != None:
#         return u'%s' % getPriceContent(data)
#     else:
#         return get_response(msg['Text']) or u'收到'



# @itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
# def atta_reply(msg):
#     return ({ 'Picture': u'图片', 'Recording': u'录音',
#         'Attachment': u'附件', 'Video': u'视频', }.get(msg['Type']) +
#         u'已下载到本地') # download function is: msg['Text'](msg['FileName'])

# @itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
# def mm_reply(msg):
#     if msg['Type'] == 'Map':
#         return u'收到位置分享'
#     elif msg['Type'] == 'Sharing':
#         return u'收到分享' + msg['Text']
#     elif msg['Type'] == 'Note':
#         return u'收到：' + msg['Text']
#     elif msg['Type'] == 'Card':
#         return u'收到好友信息：' + msg['Text']['Alias']

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    if msg['isAt']:
        code = msg['Text']
        code = removeAtNickName(code, msg['User']['Self']['NickName'])
        data = getLatestInfo(code)
        if data != None:
            return u'%s' % getPriceContent(data)
        else:
            return u'@%s\u2005%s' % (msg['ActualNickName'],
                get_response(code) or u'知道了')

    else:
        code = msg['Text']
        data = getLatestInfo(code)
        if data != None:
            return u'%s' % getPriceContent(data)

# @itchat.msg_register('Friends')
# def add_friend(msg):
#     itchat.add_friend(**msg['Text'])
#     itchat.send_msg(u'项目主页：github.com/littlecodersh/ItChat\n'
#         + u'源代码  ：回复源代码\n' + u'图片获取：回复获取图片\n'
#         + u'欢迎Star我的项目关注更新！', msg['RecommendInfo']['UserName'])
def send_room_note():
    rooms_map = dict()
    while(True):
        try:
            flag = input('是否需要获取群列表Y/N：')
            if flag == 'Y' or flag == 'y' or flag == 'yes':
                rooms_map = get_chatroom()
                print(rooms_map.keys())
            rooms = input('输入需要群发的微信群名称：')
            room_array = rooms.split(',')
            content = input('请输入需要群发的微信内容：')
            for room in room_array:
                itchat.send_msg(content, toUserName=rooms_map[room])
        except Exception as e:
            print(e)

def get_chatroom():
    chatrooms = itchat.get_chatrooms(update=True)
    room_map = dict()
    for room in chatrooms:
        room_map[room['NickName']] = room['UserName']
    return room_map


if __name__=='__main__':
    timer = threading.Timer(1, updatePriceDict)
    timer.start()
    itchat.auto_login(hotReload=True, enableCmdQR=2)
    autoReply = threading.Thread(target = itchat.run)
    autoReply.start()
    send_room_note()