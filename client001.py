from telethon import TelegramClient
import datetime
import MySQLdb
import time


# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 175613
api_hash = 'f40a3bd2c9e2ffebf1bc55e26de6e214'
chat_id = -306087265
client = TelegramClient('session_name', api_id, api_hash)
client.start()

now = datetime.datetime.now()
#print(client.get_me().stringify())
entity = client.get_entity('anryze_tokensale')
#print(entity)
chat_id = entity.id

from telethon import utils

def get_data_from_msgs(chat):
    i=1
    for message in client.get_message_history('anryze_tokensale', limit=10000, wait_time =1):
        i +=1
        print("===============================================")
        print(i)
        print("===============================================")

        print("chat id:")
        chat_id = str(chat)
        print(chat_id)
        print("msg_sender:")
        msg_sender = str(message.sender.id)
        print(msg_sender)
        print("is_bot:")
        is_bot = str(message.sender.bot)
        print(is_bot)
        print("message_id:")
        msg_id = str(message.id)
        print(msg_id)
        print("message datetime:")
        message_datetime = message.date
        print(message_datetime)
        message_datetime = int(time.mktime(time.strptime(str(message.date), '%Y-%m-%d %H:%M:%S')))
        print(message_datetime)
        print("message text:")
        mess_txt = str(message.message)
        if ("'" in mess_txt):
            continue
        print(mess_txt)
        print("reply_to_msg_id:")

        reply_to_msg_id = message.reply_to_msg_id
        print(reply_to_msg_id)

        if(reply_to_msg_id == None):
            reply_to_msg_id = 0
        else:
            reply_to_msg_id = str(message.reply_to_msg_id)

        fwd_from = 0

        '''print("fwd_from:")
        fwd_from = message.fwd_from
        print(fwd_from)
        if (fwd_from == None):
            fwd_from = 0
        else:
            fwd_from =1'''

        db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                             user="angelina",  # your username
                             passwd="ipk1898",  # your password
                             db="adm_bot",
                             charset='utf8mb4'
                             )  # name of the data base

        cur = db.cursor()

        sql = ("INSERT INTO msgs1(msg_id,mess_txt,msg_sender,message_datetime,chat_id,reply_to_msg_id,fwd_from,is_bot"
               # forward_orign_message_text"
               ") VALUES (" + str(msg_id) + ",'" + str(mess_txt) + "'," + str(msg_sender) + "," + str(message_datetime) + "," + str(chat_id) + "," + str(reply_to_msg_id) + ","+str(fwd_from)+"," + str(is_bot) + ")")
        cur.execute(sql)
        db.commit()
        #db.close()'''

get_data_from_msgs(chat_id)
'''



def get_today_msgs():
    i = 0
    for message in client.get_message_history('anryze_tokensale',offset_date = now, limit =100):
        date = str(message.date)
        date = date[0:-8]
        print (date)

        now1 = str(now)
        now1 = now1[0:-15]
        print(now1)

        if(date != now1):
            break
        print("user:")
        print(message.sender)
        print("name:")
        print(utils.get_display_name(message.sender))
        print("message_history:")
        print(message)
        i+=1
        print(i)
        print(utils.get_display_name(message.sender), message.message)

def insert_data_to_bd(msg_id, mess_txt, msg_sender, message_datetime,
                              chat_id, reply_to_msg_id, fwd_from, is_bot):

    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="angelina",  # your username
                         passwd="ipk1898",  # your password
                         db="adm_bot",
                         charset='utf8mb4'
                         )  # name of the data base

    cur = db.cursor()

    sql = ("INSERT INTO msgs(msg_id,mess_txt,msg_sender,message_datetime,chat_id,reply_to_msg_id,fwd_from,is_bot"
           # forward_orign_message_text"
           ") VALUES (" + str(msg_id) + ",'" + mess_txt + "'," + str(msg_sender) + "," + str(message_datetime) + "," + str(
        chat_id) + "," + str(reply_to_msg_id) + "," + str(fwd_from) + "," + str(is_bot) + ")")
    cur.execute(sql)
    db.commit()
    db.close()'''


