import MySQLdb


                        #
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="angelina",         # your username
                         passwd="ipk1898",  # your password
                         db="adm_bot",
                         charset='utf8mb4'
                         )

cur = db.cursor()

sql_count_all_messages = "select count(*) from msgs1 "
cur.execute(sql_count_all_messages)
count_all_messages  = cur.fetchall()
print("count all messages:")
count_all_messages = str(count_all_messages)[2:-4]
print(count_all_messages)

sql_count_msg_community_1 = "select count(*) from msgs1 where msg_sender = 236961704"
cur.execute(sql_count_msg_community_1)
count_msg_community_1  = cur.fetchall()
print("count all messages from community 1:")
count_msg_community_1 = str(count_msg_community_1)[2:-4]
print(count_msg_community_1)

sql_count_reply_community_1 = "select count(*) from msgs1 where msg_sender = 236961704 and reply_to_msg_id=0"
cur.execute(sql_count_reply_community_1)
count_reply_community_1  = cur.fetchall()
print("replies from community:")
count_reply_community_1 = str(count_reply_community_1)[2:-4]
replies_from_community = int(count_msg_community_1)-int(count_reply_community_1)
print(replies_from_community)

import datetime
import time

#------------------------------------------ALL MESSAGES INFO
dts = datetime.datetime.utcnow()
today = round(time.mktime(dts.timetuple()) + dts.microsecond/1e6)
last_day = today - 60*60*60*24
sql_count_msg_day= "select count(*) from msgs1 where  message_datetime >1519084800 ;"
cur.execute(sql_count_msg_day)
count_msg_day  = cur.fetchall()
print("count all messages from today:")
count_msg_day = str(count_msg_day)[2:-4]
print(count_msg_day)
count_msg_day = int(count_msg_day)

sql_count_msg_week= "select count(*) from msgs1 where message_datetime < 1519084800 and message_datetime > 1518566400;"
cur.execute(sql_count_msg_week)
count_msg_week  = cur.fetchall()
print("count all messages from week:")
count_msg_week = str(count_msg_week)[2:-4]
print(count_msg_week)
count_msg_week = int(count_msg_week)

sql_count_msg_month= "select count(*) from msgs1 where message_datetime < 1519084800 and message_datetime > 1516492800;"
cur.execute(sql_count_msg_month)
count_msg_month = cur.fetchall()
print("count all messages from month:")
count_msg_month = str(count_msg_month)[2:-4]
print(count_msg_month)
count_msg_month = int(count_msg_month)

count_msgs = {'day' : count_msg_day, 'week' : count_msg_week, 'month' : count_msg_month}
print(count_msgs)

#======================USERS ACTIVITIES

messages_from_unique_users_sql_d ="select count(distinct msg_sender) from msgs1 " \
                                "where message_datetime >1519084800 ;"
cur.execute(messages_from_unique_users_sql_d)
msgs_from_unique_users_d  = cur.fetchall()
msgs_from_unique_users_d = str(msgs_from_unique_users_d)[2:-4]
msgs_from_unique_users_d = int(msgs_from_unique_users_d)
print("count messages from unique users by day:")
print(msgs_from_unique_users_d)
print("% messages from unique users compare to all msgs by day:")

unique_msgs_compare_to_all_msgs_d = (msgs_from_unique_users_d/count_msg_day)*100
print(unique_msgs_compare_to_all_msgs_d)

messages_from_unique_users_sql_w ="select count(distinct msg_sender) from msgs1 " \
                                "where message_datetime < 1519084800 and message_datetime > 1518566400;"
cur.execute(messages_from_unique_users_sql_w)
msgs_from_unique_users_w  = cur.fetchall()
msgs_from_unique_users_w = str(msgs_from_unique_users_w)[2:-4]
msgs_from_unique_users_w = int(msgs_from_unique_users_w)
print("count messages from unique users by week:")
print(msgs_from_unique_users_w)

unique_msgs_compare_to_all_msgs_w = (msgs_from_unique_users_w/count_msg_week)*100
print("% messages from unique users compare to all msgs by week:")
print(unique_msgs_compare_to_all_msgs_w)

messages_from_unique_users_sql_m ="select count(distinct msg_sender) from msgs1 " \
                                "where message_datetime < 1519084800 and message_datetime > 1516492800;"
cur.execute(messages_from_unique_users_sql_m)
msgs_from_unique_users_m  = cur.fetchall()
msgs_from_unique_users_m = str(msgs_from_unique_users_m)[2:-4]
msgs_from_unique_users_m = int(msgs_from_unique_users_m)
print("count messages from unique users by month:")
print(msgs_from_unique_users_m)

unique_msgs_compare_to_all_msgs_m = (msgs_from_unique_users_m/count_msg_month)*100
print("% messages from unique users compare to all msgs by month:")
print(unique_msgs_compare_to_all_msgs_m)

msgs_from_unique_users = {'day':msgs_from_unique_users_d,'week':msgs_from_unique_users_w,'month':msgs_from_unique_users_m}

msgs_from_unique_percent = {'day':unique_msgs_compare_to_all_msgs_m,'week':unique_msgs_compare_to_all_msgs_w,
                            'month':unique_msgs_compare_to_all_msgs_m}

#=====================MESSAGES FROM ADMINS BY DATA

sql_count_msg_day_com= "select count(*) from msgs1 where  message_datetime >1519084800 and msg_sender = 236961704;"
cur.execute(sql_count_msg_day_com)
count_msg_day_com  = cur.fetchall()
print("count all messages from today by community 1:")
count_msg_day_com = str(count_msg_day_com)[2:-4]
count_msg_day_com = int(count_msg_day_com)

print(count_msg_day_com)

sql_count_msg_week_com= "select count(*) from msgs1 where" \
                    " message_datetime < 1519084800 and message_datetime > 1518566400 and msg_sender = 236961704;"
cur.execute(sql_count_msg_week_com)
count_msg_week_com  = cur.fetchall()
print("count all messages from week by community 1:")
count_msg_week_com = str(count_msg_week_com)[2:-4]
count_msg_week_com = int(count_msg_week_com)
print(count_msg_week_com)

sql_count_msg_month_com= "select count(*) from msgs1 where" \
                     " message_datetime < 1519084800 and message_datetime > 1516492800 and msg_sender = 236961704;"
cur.execute(sql_count_msg_month_com)
count_msg_month_com = cur.fetchall()
print("count all messages from month by community 1:")
count_msg_month_com = str(count_msg_month_com)[2:-4]
count_msg_month_com = int(count_msg_month_com)
print(count_msg_month_com)
msgs_from_communities = {'day':count_msg_day_com,'week':count_msg_week_com,'month':count_msg_month_com}
#select count(*) from test3 where MATCH ('thanks') and date >="+str(month)+" and chat="+str(chat)+";"

#------------------- USERS QUESTIONS

sql_count_questions_today= "select count(*) from msgs1 where " \
                     "mess_txt like'%?%' and msg_sender != 236961704 and message_datetime >1519084800;"
cur.execute(sql_count_questions_today)
count_questions_today = cur.fetchall()
print("count questions today:")
count_questions_today = str(count_questions_today)[2:-4]
print(count_questions_today)

sql_count_questions_week= "select count(*) from msgs1 where " \
                     "mess_txt like'%?%' and msg_sender != 236961704 and " \
                        "message_datetime < 1519084800 and message_datetime > 1518566400;"
cur.execute(sql_count_questions_week)
count_questions_week = cur.fetchall()
print("count questions by week:")
count_questions_week = str(count_questions_week)[2:-4]
print(count_questions_week)


sql_count_questions_month= "select count(*) from msgs1 where " \
                     "mess_txt like'%?%' and msg_sender != 236961704 and " \
                        "message_datetime < 1519084800 and message_datetime > 1516492800;"
cur.execute(sql_count_questions_month)
count_questions_month = cur.fetchall()
print("count questions by month:")
count_questions_month = str(count_questions_month)[2:-4]
count_questions_month = int(count_questions_month)
print(count_questions_month)

questions = {'day':count_questions_today,'week':count_questions_week,'month':count_questions_month}
#------------------- COMMUNITY REPLIES

sql_count_comm_rep_today= "select count(*) from msgs1 where " \
                     "reply_to_msg_id!=0 and msg_sender = 236961704 and message_datetime >1519084800;"
cur.execute(sql_count_comm_rep_today)
count_comm_rep_today = cur.fetchall()
print("count replies from community today:")
count_comm_rep_today = str(count_comm_rep_today)[2:-4]
print(count_comm_rep_today)

sql_count_comm_rep_week= "select count(*) from msgs1 where " \
                     "reply_to_msg_id!=0 and msg_sender = 236961704 " \
                          "and message_datetime < 1519084800 and message_datetime > 1518566400;"
cur.execute(sql_count_comm_rep_week)
count_comm_rep_week = cur.fetchall()
print("count replies from community week:")
count_comm_rep_week = str(count_comm_rep_week)[2:-4]
print(count_comm_rep_week)

sql_count_comm_rep_month= "select count(*) from msgs1 where " \
                     "reply_to_msg_id!=0 and msg_sender = 236961704 and  " \
                          "message_datetime < 1519084800 and message_datetime > 1516492800;"
cur.execute(sql_count_comm_rep_month)
count_comm_rep_month = cur.fetchall()
print("count replies from community month:")
count_comm_rep_month = str(count_comm_rep_month)[2:-4]
print(count_comm_rep_month)

communities_replies = {'day':count_comm_rep_today,'week':count_comm_rep_week,'month':count_comm_rep_month}


#------------------- THANKS WORDS


sql_count_thanks_today= "select count(*) from msgs1 where " \
                     "mess_txt like'%thank%' and msg_sender != 236961704 and message_datetime >1519084800;"
cur.execute(sql_count_thanks_today)
count_thanks_today = cur.fetchall()
print("count thank words by today:")
count_thanks_today = str(count_thanks_today)[2:-4]
print(count_thanks_today)

sql_count_thanks_week= "select count(*) from msgs1 where " \
                     "mess_txt like'%thank%' and msg_sender != 236961704 and " \
                        "message_datetime < 1519084800 and message_datetime > 1518566400;"
cur.execute(sql_count_thanks_week)
count_thanks_week = cur.fetchall()
print("count thank words by week:")
count_thanks_week = str(count_thanks_week)[2:-4]
print(count_thanks_week)


sql_count_thanks_month= "select count(*) from msgs1 where " \
                     "mess_txt like'%thank%' and msg_sender != 236961704 and " \
                        "message_datetime < 1519084800 and message_datetime > 1516492800;"
cur.execute(sql_count_thanks_month)
count_thanks_month = cur.fetchall()
print("count thank words by month:")
count_thanks_month = str(count_thanks_month)[2:-4]
print(count_thanks_month)

thanks = {'day':count_thanks_today,'week':count_thanks_week,'month':count_thanks_month}

#------------------- USER TO USER REPLIES

sql_count_u_rep_today= "select count(*) from msgs1 where " \
                     "reply_to_msg_id!=0 and msg_sender != 236961704 and message_datetime >1519084800;"
cur.execute(sql_count_u_rep_today)
count_u_rep_today = cur.fetchall()
print("count replies from users today:")
count_u_rep_today = str(count_comm_rep_today)
print(count_u_rep_today)

sql_count_u_rep_week= "select count(*) from msgs1 where " \
                     "reply_to_msg_id!=0 and msg_sender != 236961704 " \
                          "and message_datetime < 1519084800 and message_datetime > 1518566400;"
cur.execute(sql_count_comm_rep_week)
count_u_rep_week = cur.fetchall()
print("count replies from users by week:")
count_u_rep_week = str(count_u_rep_week)[2:-4]
print(count_u_rep_week)

sql_count_u_rep_month= "select count(*) from msgs1 where " \
                     "reply_to_msg_id!=0 and msg_sender != 236961704 and  " \
                          "message_datetime < 1519084800 and message_datetime > 1516492800;"
cur.execute(sql_count_u_rep_month)
count_u_rep_month = cur.fetchall()
print("count replies from users month:")
count_u_rep_month = str(count_u_rep_month)[2:-4]
print(count_u_rep_month)
users_replies = {'day':count_u_rep_today,'week':count_u_rep_week,'month':count_u_rep_month}


#------------------- COMMUNITY MENTIONED

#-------------------- MAKE INFO ARRAY
messages = {'count_msgs':count_msgs,'msgs_from_unique_users':msgs_from_unique_users,
            'msgs_from_unique_users_percent':msgs_from_unique_percent,
            'msgs_from_communities':msgs_from_communities}
questions = {'questions':questions}
thanks_words = {'thanks':thanks}
communities_replies = {'communities_replies':communities_replies}
users_replies = {'users_replies':users_replies}

messages_from_bots = {'day':0,'week':0,'month':0}
messages_from_bots = {'messages_from_bots':messages_from_bots}


all_data = {'messages':messages,'questions':questions,'thanks_words':thanks_words,
            'communities_replies':communities_replies,'users_replies':users_replies,
            'messages_from_bots': messages_from_bots}
print(all_data)

import json

print(json.dumps(all_data,sort_keys=True, indent=4))

json = json.dumps(all_data,sort_keys=True, indent=4)
print(json)

f = open('messages.json', 'w')
f.write(json)
f.close()
#db.commit()  # you need to call commit() method to save your changes to the database
#SELECT reply_to_msg_id, count(*) c FROM msgs1 GROUP BY reply_to_msg_id  ORDER BY c DESC LIMIT 10;

db.close()