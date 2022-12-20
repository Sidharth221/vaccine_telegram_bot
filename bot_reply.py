#ALL THE LOGIC FOR ASKING QUESTIONS TO USER AND GETTING HIS RESPONSE IS IN THIS FILE

import datetime

#CREATING A VARIABLE TO KNOW WHICH QUESTION TO ASK USER AND SAVE USER RESPONSE ACCORDINGLY
#ITS VALUE GETS INCREASED BY 1 AFTER EACH QUESTION AND AT LAST IT AGAIN BECOMES ZERO  
count1 = 0

def bot_responses(update):
    global count1
    if count1==0:
        name = str(update.message.text).lower()
        update.message.reply_text('Please type in Your location')
        count1 = count1 + 1
        return {"name":name}

    if count1==1:
        location = str(update.message.text).lower()
        update.message.reply_text(' Send 1 for booking slot \n Send 2 for viewing slot')
        count1 = count1 + 1
        return {"location":location}

    if count1==2:
        service = str(update.message.text).lower()
        #TO GET DATE AT WHICH USER IS BOOKING VACCINE
        today = datetime.date.today()
        bot_date = f"BOOK DATE FOR VACCINE \n Send 1 for {today + datetime.timedelta(days=1)} \n Send 2 for {today + datetime.timedelta(days=2)} \n Send 3 for {today + datetime.timedelta(days=3)}"
        update.message.reply_text(bot_date)
        count1 = count1 + 1
        return {"service":service}

    if count1==3:
        today = datetime.date.today()
        user_date = str(update.message.text).lower()
        if user_date == "1":
            vaccine_date = today + datetime.timedelta(days=1)
            update.message.reply_text('BOOK TIME FOR VACCINE \n Send 1 for 11am \n Send 2 for 2pm \n Send 3 for 5pm')
            count1 = count1 + 1
            return {"vaccine_date":vaccine_date}
        elif user_date == "2":
            vaccine_date = today + datetime.timedelta(days=2)
            
            update.message.reply_text('BOOK TIME FOR VACCINE \n Send 1 for 11am \n Send 2 for 2pm \n Send 3 for 5pm')
            count1 = count1 + 1
            return {"vaccine_date":vaccine_date}
        elif user_date == "3":
            vaccine_date = today + datetime.timedelta(days=3) 
            update.message.reply_text('BOOK TIME FOR VACCINE \n Send 1 for 11am \n Send 2 for 2pm \n Send 3 for 5pm')
            count1 = count1 + 1
            return {"vaccine_date":vaccine_date}
        else:
            today = datetime.date.today()
            bot_date = f"PLEASE SEND FROM THE OPTIONS BELOW ONLY \n Send 1 for {today + datetime.timedelta(days=1)} \n Send 2 for {today + datetime.timedelta(days=2)} \n Send 3 for {today + datetime.timedelta(days=3)}"
            update.message.reply_text(bot_date)
            vaccine_date = None
            return {"vaccine_date":vaccine_date}
        

    if count1==4:
        user_time = str(update.message.text).lower()
        if user_time == "1":
            vaccine_time = "11am"
            #count1 BECOMES 0 TO AGAIN START BOOKING FOR ANOTHER USER
            count1 = 0
            return {"vaccine_time":vaccine_time}
        elif user_time == "2":
            vaccine_time = "2pm"
            
            count1 = 0
            return {"vaccine_time":vaccine_time}
        elif user_time == "3":
            vaccine_time = "5pm"
            
            count1 = 0
            return {"vaccine_time":vaccine_time}
        else:
            update.message.reply_text('PLEASE SEND FROM THE OPTIONS BELOW ONLY \n Send 1 for 11am \n Send 2 for 2pm \n Send 3 for 5pm')
            vaccine_time = None
            print(vaccine_time)
            return {"vaccine_time":vaccine_time}  
                       

            
           

    