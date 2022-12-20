from telegram.ext import *
import bot_reply as b
import mysql.connector as mcc
import datetime
import time

#MYSQL DATABASE CONNECTION
conn=mcc.connect(host="localhost",user="root",passwd="Enter your db password",database="vaccine_book")
cursor=conn.cursor()

#CREATING AN EMPTY DICTIONARY TO STORE USER RESPONSES
d1={}

#CHECKING IF TABLE EXISTS IN MYSQL DATABASE
stmt = "SHOW TABLES LIKE 'vaccine_details'"
cursor.execute(stmt)
result = cursor.fetchone()
if result:
    print("exists")    
else:
    #IF TABLE DOES NOT EXIST IT WILL CREATE ONE     
    sql="CREATE TABLE vaccine_details (id int NOT NULL AUTO_INCREMENT,name varchar(255),location varchar(255), vacine_date date, vaccine_time varchar(255), is_booked boolean not null default 0, PRIMARY KEY (id))"
    cursor.execute(sql)
    conn.commit()

#API KEY OF BOT 
API_KEY = "5552800779:AAF3JjoG7IOn_fc2_cSW_hSBHkCwNYDPo8s"

#BOT USERNAME = vaccine_book_bot

print("Bot Started")

# /book WILL START VACCINE BOOKING
def start_command(update, context):
    update.message.reply_text(f"Send \'/book\' or \'/Book\' to start vaccine booking")

def book_command(update, context):
    update.message.reply_text('Please type in Your Name')    
    

def help_command(update, context):
    update.message.reply_text('help')    


def handle_message(update, context):
    text = str(update.message.text).lower() 
    
    y = b.bot_responses(update)  #CALLING AND SAVING RESPONSE OF THIS FUNCTION WHICH IS IMPORTED FROM 'bot_reply.py'

    d1.update(y)  #STORING USER RESPONSE IN DICTIONARY
    d1.pop('service', None)
    print(d1)
    try:
        if d1["vaccine_time"] != None:   #WHEN THE USER SELECTS VACCINE TIME IT WILL SAVE ALL USER RESPONSE IN DATABASE
            name = d1["name"]
            location = d1["location"]
            vaccine_date = d1["vaccine_date"]
            vaccine_time = d1["vaccine_time"]
            
            #SQL QUERY FOR SAVING IN DATABASE
            sql = f'INSERT INTO vaccine_details (name, location, vacine_date, vaccine_time, is_booked) VALUES (\'{name}\',\'{location}\',\'{vaccine_date}\',\'{vaccine_time}\',True)'
            print(sql)
            cursor.execute(sql)
            conn.commit()

            #DISPLAYING FINAL MESSAGE
            update.message.reply_text(f"Your vaccine slot has been booked for {vaccine_date} at {vaccine_time} successfully")

            time.sleep(10)
            update.message.reply_text(f"Send \'/book\' or \'/Book\' to book vaccine for another user")
            
            d1["vaccine_time"]=None
            print('success')

    except:
        pass    

    
#MAIN FUNCTION OF BOT
def main():
     
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("book", book_command))
    dp.add_handler(CommandHandler("Book", book_command))
    dp.add_handler(CommandHandler("help", help_command))

    ot = dp.add_handler(MessageHandler(Filters.text, handle_message))
    print(ot)
    updater.start_polling()    
    updater.idle()

main()    



