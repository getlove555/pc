# -*- coding: utf-8 -*-
from LIBERATION import *
from datetime import datetime
import json, time, random, tempfile, os, sys, pytz
import codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast
from gtts import gTTS
from googletrans import Translator


client = LineClient()
#client = LineClient(id='EMAILMU', passwd='PASSWORDMU')
#client = LineClient(authToken='TOKENMU') 
client.log("Auth Token : " + str(client.authToken))
#========================================================
channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))
#========================================================
clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = LinePoll(client)
clientMID = client.profile.mid

contact = client.getProfile()
backup = client.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
#====================================

helpMessage =""" ༺༽།☤ⵓః•TOME BOTLINE•ఃⵓ☤།༼༻
╭════════╬♥╬════════╮
                       ʜᴇʟᴘ menu
╰════════╬♥╬════════╯
╭════════╬♥╬════════╮
║♪「Myhelp」 ช่วยเหลือ
║♪「Me」 ตัวเอง
║♪「 Mymid」 ขอเอมไอดี
║♪「 Myname」 เปลี่ยนชื่อ
║♪「 Mybio」 เปลี่ยนตัส
║♪「 Mypicture」 ขอรูปตัวเอง
║♪「 Myvideoprofile」 ขอ vdo ประจำตัว
║♪「 Mycover」 ก๊อฟรูป
║♪「 Stealprofile「@」 เอารูปเพื่อน
║♪「Unsend me」
║♪「 Getsq」
║♪「Lc 「@」
║♪「 Gc 「@」
║♪「 Sticker: 「angka」 สติกเก้อ
║♪「 Yt: 「text」 ยูทูป ใส่ชื่อ
║♪「 Image: 「textเปลี่ยนข้อความเป็นรูป
║♪「Say: text」พูดตาม
║♪「 Apakah text」 
║♪「 Sytr: text」
║♪「 Tr: text」
║♪「 Speed」ความอร็ว
║♪「 Spic @」 เอารูปเพื่อน
║♪「 Scover @」
║♪「 Tagall」
║♪「 Ceksider」
║♪「 Offread」
║♪「 Restart」
║♪「 Friendlist」
║♪「 Cloneprofile @」
║♪「 Restoreprofile」
║♪「 Lurking on」
║♪「 Lurking」
║♪「 lurking off」
║♪「 Lurking reset」
║♪「 kick @」
║♪「 Mode:self」
║♪「 Mode:public」
╰════════╬♥╬════════╯
╭════════╬♥╬════════╮
          🔪JANGAN ADA TYPO 🔪
╰════════╬♥╬════════╯
╭�