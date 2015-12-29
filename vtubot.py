#!usr/bin/python
import telepot
import time
import sys
from pprint import pprint
from twill import get_browser
from twill.commands import go, showforms, formclear, fv, submit
from twill.commands import *

#'TOKEN' is taken after chatting with bot father in telegram app

bot = telepot.Bot('TOKEN')
b = get_browser()

def handle(msg):
 print "Handle funct"
 content_type, chat_type, chat_id = telepot.glance2(msg)
 data = open("users.txt", "a")
 if str(chat_id) in open('users.txt').read():
  print "User exists"
 else:
  data.write(str(chat_id)+" ")
  data.write(str(msg['chat']['first_name'])+" "+str(msg['chat']['last_name'])+"\n")
 cmd=str(msg['text'])

 if cmd == 'Results':
  bot.sendMessage(chat_id, "Enter USN number to see your results.")

 elif len(cmd) == 10:
  bot.sendMessage(chat_id, "Processing")
  go("http://results.vtu.ac.in/")
  formclear('1')
  fv("1", "rid", cmd)
  submit('submit')
  save_html(cmd+".html")
  lines = open(cmd+'.html').readlines()
  open(cmd+'.html', 'w').writelines(lines[241:-84])
  open(cmd+'.html', 'a').writelines("@vtu_bot- if this file is empty please check the USN or try again when the results are announced ")
  f = open(cmd+'.html', 'rb')
  response = bot.sendDocument(chat_id, f)
 else:
  bot.sendMessage(chat_id, "Please enter a valid USN number")


bot.notifyOnMessage(handle)
print 'Waiting..'


while 1:
 time.sleep(1)
