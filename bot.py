import pymongo
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import ChatMember
from pyrogram import *
import asyncio
import psutil
import traceback
from pyrogram.types import *
import requests
import os, time
from datetime import datetime
import pytz
import random



import os
import openai
import uptime
import datetime
import pythonping
import psutil
import time 
import speedtest

# Bot API Token
API_TOKEN = '7401875465:AAHoetLWlNFRSliGU7VQaLtH-pXaDlXpLGU'
API_ID = '24771953'
API_HASH = '2dd99aa9f140d0eacb46368d1dd0994b'
# OpenAI API Key
openai.api_key = "sk-proj-PPnyhG59SsqsjfCR1nhhT3BlbkFJ7gP1iskxVp35Kg39Fg93"
#Only owner id
NOBITA = "1965898154"
# MongoDB setup
MONGODB_URI = ""  # Set your MongoDB connection string here
client = pymongo.MongoClient(MONGODB_URI)
db = client["wormgpt"]
collection = db["allowed_users"]
allowed_users = ["@Riyal_Nobi", ""]
owners = ["@riyal_nobi", ""]

for user in collection.find({}):
    allowed_users.append(user["telegram_username"])

# Define a function to check if a user is an owner
def is_owner(username):
    return username in owners

async def synchronize_time():
    await app.get_me()

    asyncio.run(synchronize_time())
# Create a Pyrogram Client
app = Client(
    "my_bot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = API_TOKEN
)

def get_total_cpu_usage():
    with open('/proc/stat') as file:
        line = file.readline()
        cpu_stats = line.split()
        total_cpu_time = sum(int(cpu) for cpu in cpu_stats[1:])
        idle_cpu_time = int(cpu_stats[4])
        return 100.0 * (1 - idle_cpu_time / total_cpu_time)
    
def get_total_cpu_usage():
    return psutil.cpu_percent(interval=1)

bot_start_time = datetime.datetime.now()


def get_server_uptime():
    uptime_seconds = psutil.boot_time()
    return time.time() - uptime_seconds
# Function to ping a server
def ping_server(host):
    return pythonping.ping(host, count=4) 
 # You can change the count as needed

def get_bot_cpu_usage():
    bot_process = psutil.Process(os.getpid())
    return bot_process.cpu_percent(interval=1)

def get_response(msg):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=msg,
        max_tokens=3500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return completion.choices[0].text

    
@app.on_message(filters.command(['code']))
def cod3(_,message):
    if message.from_user.username in allowed_users:
        question = message.text[len("/code"):]
        if len(question) == 0:
            message.reply( "â—ðš‚ðšŽðš—ðš ð™»ðš’ðš”ðšŽ ðšƒðš‘ðš’ðšœ: /code ðšˆðš˜ðšžðš› ðš€ðšžðšŽðšœðšðš’ðš˜ðš—")
        else:
            answer = get_response(question+",use markdown to  identify the code ")
            message.reply( answer)
            cdd = answer.split('``')[1]
            with open('Your-Code.txt','w') as f:
                f.write(cdd)
            message.reply_document('Your-Code.txt',caption='**ð™€ð™­ð™˜ð™šð™§ð™˜ð™žð™¨ð™š ð™‡ð™šð™›ð™© ðŸ˜ˆ**\n1.Save This Code ðŸ’¾ \n2.Run The Code ðŸ›  \n3.In Your Best IDE ðŸ’» \nðŸ’  ï¼·ï¼¯ï¼²ï¼­ ï¼§ï¼°ï¼´')
        
   
    else:
        message.reply( "âŒ ðš‚ðš˜ðš›ðš›ðš¢, ðš¢ðš˜ðšž ðšŠðš›ðšŽ ðš—ðš˜ðš ðšŠðšžðšðš‘ðš˜ðš›ðš’ðš£ðšŽðš ðšðš˜ ðš‹ðš˜ðš \nðŸŒŸ ð™±ðšžðš¢ ð™±ðš˜ðš ð™µðš›ðš˜ðš– @DARK_WORM_GPT_A")
        

@app.on_message(filters.command("start"))
def start_bot(client, message):
    # Create an InlineKeyboardMarkup with the "Start" button
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="â‡ Support NetWork â‡", url=f"https://t.me/NOBINOBOTSUPPORT"),
            ],
            [
                InlineKeyboardButton(text="ðŸ’  Creator Of Bot ðŸ’ ", url=f"https://t.me/RIYAL_NOBI"),
            ],
            [
                InlineKeyboardButton(text="ðŸ”° NOBINO HELP ðŸ”°", callback_data="help"),
                InlineKeyboardButton(text="ðŸ’» ABOUT NOBINOð WORM GPT Ÿ’»", callback_data="about"),
            ],
            [
             InlineKeyboardButton(text="ðŸ’  NOBINO WORM GPT AI DEV ðŸ’ ", callback_data="admin"),
             InlineKeyboardButton(text="ðŸŒŸ User Commands ðŸŒŸ", callback_data="auth"),
            ],
        ]
    )

    start_message = app.send_message(
        message.chat.id,
        """ðŸ’• ð™·ðšŽðš•ðš•ðš˜ ðš‚ðš’ðš› â— ðš†ðšŽðš•ðšŒðš˜ðš–ðšŽ ðšƒðš˜ ðš†ðš˜ðš›ðš– ð™¶ð™¿ðšƒ ð™°ðš’ ! ð™¿ðš•ðšŽðšŠðšœðšŽ Click On The Bot User Commands Button ð™µðš˜ðš› ðš‚ðšŽðšŽ ð™µðšŽðšŠðšðšžðš›ðšŽðšœ""",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("auth"))
def auth_callback(client, callback_query):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="â¬…ï¸", callback_data="back"),
            ],
        ]
    )

    app.send_message(
        callback_query.message.chat.id,
        """
âœ… ðšƒðš‘ðšŽðš›ðšŽ ðšŠðš›ðšŽ ðšŠðš•ðš• ðšŒðš–ðšðšœ ðšŠðšžðšðš‘ ðšžðšœðšŽðš›ðšœ

âœ… ð™³ðš’ðš›ðšŽðšŒðšðš•ðš¢ ð™°ðšœðš” ðš€ðšžðšŽðšœðšðš’ðš˜ðš—ðšœ 

âœ… ð™µðš˜ðš› ð™²ðš˜ðšðšŽ ð™´ðš¡ðš™ðš•ðšŠðš—ðšŠðšðš’ðš˜ðš— ð™°ðš—ðš ð™²ðš˜ðšðšŽ ð™µðš’ðš•ðšŽ ðš„ðš™ðš•ðš˜ðšŠðš ðš„ðšœðšŽ

âœ… /code : ðš€ðšžðšŽðšœðšðš’ðš˜ðš—......

        """,
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("admin"))
def admin_callback(client, callback_query):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="â¬…ï¸", callback_data="back"),
            ],
        ]
    )

    app.send_message(
        callback_query.message.chat.id,
        """
ðŸŒŸ ð™³ð™°ðšð™º ðš†ð™¾ðšð™¼ ð™¶ð™¿ðšƒ ð™°ð™¸ ð™³ð™´ðš…ð™´ð™»ð™¾ð™¿ð™´ðš ðŸŒŸ 

ðŸ’  ð•„ð”¸ð•€â„• ð”»ð”¼ð• :- @RIYAL_NOBI


        """,
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("about"))
def about_callback(client, callback_query):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
         
            [
                InlineKeyboardButton(text="â¬…ï¸", callback_data="back"),
            ],
        ]
    )

    app.send_message(
        callback_query.message.chat.id,
        """
ð˜¼ð™£ ð™šð™«ð™žð™¡ ð˜¾ð™ð™–ð™©ð™‚ð™‹ð™-ð™¡ð™žð™ ð™š ð˜¼ð™„ ð™¢ð™¤ð™™ð™šð™¡ ð™žð™¨ ð™¨ð™¥ð™§ð™šð™–ð™™ð™žð™£ð™œ ð™–ð™˜ð™§ð™¤ð™¨ð™¨ ð™©ð™ð™š ð™™ð™–ð™§ð™  ð™¬ð™šð™— ð™–ð™£ð™™ ð™šð™£ð™–ð™—ð™¡ð™žð™£ð™œ ð™ð™–ð™˜ð™ ð™šð™§ð™¨ ð™©ð™¤ ð™¥ð™šð™§ð™›ð™¤ð™§ð™¢ ð™˜ð™®ð™—ð™šð™§ð™–ð™©ð™©ð™–ð™˜ð™ ð™¨ ð™¤ð™£ ð™– ð™£ð™šð™«ð™šð™§-ð™—ð™šð™›ð™¤ð™§ð™š-ð™¨ð™šð™šð™£ ð™¨ð™˜ð™–ð™¡ð™š


ð™ð™šð™­ð™©ð™Žð™¤ð™›ð™žð™– ð™ˆð™–ð™ð™žð™§ð™¤ð™«ð™– 
ð™„ð™£ ð™¢ð™¤ð™§ð™š ð˜¼ð™„-ð™§ð™šð™¡ð™–ð™©ð™šð™™ ð™™ð™¤ð™¤ð™¢ð™¨ð™–ð™®ð™šð™§ ð™£ð™šð™¬ð™¨, ð™– ð˜¾ð™ð™–ð™©ð™‚ð™‹ð™-ð™¨ð™©ð™®ð™¡ð™š ð˜¼ð™„ ð™©ð™¤ð™¤ð™¡ ð™žð™¨ ð™©ð™–ð™ ð™žð™£ð™œ ð™¤ð™›ð™› ð™–ð™˜ð™§ð™¤ð™¨ð™¨ ð™˜ð™®ð™—ð™šð™§ð™˜ð™§ð™žð™¢ð™š ð™›ð™¤ð™§ð™ªð™¢ð™¨ ð™¤ð™£ ð™©ð™ð™š ð™™ð™–ð™§ð™  ð™¬ð™šð™—. ð˜¾ð™–ð™¡ð™¡ð™šð™™ ð™’ð™¤ð™§ð™¢ð™‚ð™‹ð™, ð™©ð™ð™š â€œð™¨ð™¤ð™¥ð™ð™žð™¨ð™©ð™žð™˜ð™–ð™©ð™šð™™ ð˜¼ð™„ ð™¢ð™¤ð™™ð™šð™¡â€ ð™žð™¨ ð™™ð™šð™¨ð™žð™œð™£ð™šð™™ ð™©ð™¤ ð™¥ð™§ð™¤ð™™ð™ªð™˜ð™š ð™ð™ªð™¢ð™–ð™£-ð™¡ð™žð™ ð™š ð™©ð™šð™­ð™© ð™©ð™ð™–ð™© ð™˜ð™–ð™£ ð™—ð™š ð™ªð™¨ð™šð™™ ð™žð™£ ð™ð™–ð™˜ð™ ð™žð™£ð™œ ð™˜ð™–ð™¢ð™¥ð™–ð™žð™œð™£ð™¨, ð™šð™£ð™–ð™—ð™¡ð™žð™£ð™œ ð™ð™–ð™˜ð™ ð™šð™§ð™¨ ð™©ð™¤ ð™¥ð™šð™§ð™›ð™¤ð™§ð™¢ ð™–ð™©ð™©ð™–ð™˜ð™ ð™¨ ð™¤ð™£ ð™– ð™£ð™šð™«ð™šð™§-ð™—ð™šð™›ð™¤ð™§ð™š-ð™¨ð™šð™šð™£ ð™¨ð™˜ð™–ð™¡ð™š.

â€œð™ð™ð™žð™¨ ð™©ð™¤ð™¤ð™¡ ð™¥ð™§ð™šð™¨ð™šð™£ð™©ð™¨ ð™žð™©ð™¨ð™šð™¡ð™› ð™–ð™¨ ð™– ð™—ð™¡ð™–ð™˜ð™ ð™ð™–ð™© ð™–ð™¡ð™©ð™šð™§ð™£ð™–ð™©ð™žð™«ð™š ð™©ð™¤ ð™‚ð™‹ð™ ð™¢ð™¤ð™™ð™šð™¡ð™¨, ð™™ð™šð™¨ð™žð™œð™£ð™šð™™ ð™¨ð™¥ð™šð™˜ð™žð™›ð™žð™˜ð™–ð™¡ð™¡ð™® ð™›ð™¤ð™§ ð™¢ð™–ð™¡ð™žð™˜ð™žð™¤ð™ªð™¨ ð™–ð™˜ð™©ð™žð™«ð™žð™©ð™žð™šð™¨,â€ ð™¨ð™šð™˜ð™ªð™§ð™žð™©ð™® ð™§ð™šð™¨ð™šð™–ð™§ð™˜ð™ð™šð™§ ð˜¿ð™–ð™£ð™žð™šð™¡ ð™†ð™šð™¡ð™¡ð™šð™® ð™¨ð™–ð™žð™™ ð™¬ð™§ð™¤ð™©ð™š ð™¤ð™£ ð˜¾ð™®ð™—ð™šð™§ð™¨ð™šð™˜ð™ªð™§ð™žð™©ð™® ð™¨ð™žð™©ð™š, ð™Žð™¡ð™–ð™¨ð™ð™£ð™šð™­ð™©. â€œð™’ð™¤ð™§ð™¢ð™‚ð™‹ð™ ð™¬ð™–ð™¨ ð™–ð™¡ð™¡ð™šð™œð™šð™™ð™¡ð™® ð™©ð™§ð™–ð™žð™£ð™šð™™ ð™¤ð™£ ð™– ð™™ð™žð™«ð™šð™§ð™¨ð™š ð™–ð™§ð™§ð™–ð™® ð™¤ð™› ð™™ð™–ð™©ð™– ð™¨ð™¤ð™ªð™§ð™˜ð™šð™¨, ð™¥ð™–ð™§ð™©ð™žð™˜ð™ªð™¡ð™–ð™§ð™¡ð™® ð™˜ð™¤ð™£ð™˜ð™šð™£ð™©ð™§ð™–ð™©ð™žð™£ð™œ ð™¤ð™£ ð™¢ð™–ð™¡ð™¬ð™–ð™§ð™š-ð™§ð™šð™¡ð™–ð™©ð™šð™™ ð™™ð™–ð™©ð™–.â€

ð™’ð™ð™–ð™© ð™™ð™¤ð™šð™¨ ð™©ð™ð™žð™¨ ð™¢ð™šð™–ð™£ ð™›ð™¤ð™§ ð™©ð™ð™š ð™§ð™šð™¨ð™© ð™¤ð™› ð™ªð™¨? ð™€ð™¨ð™¨ð™šð™£ð™©ð™žð™–ð™¡ð™¡ð™® ð™žð™© ð™—ð™¤ð™žð™¡ð™¨ ð™™ð™¤ð™¬ð™£ ð™©ð™¤ ð™©ð™ð™š ð™¨ð™¥ð™šð™šð™™ ð™–ð™£ð™™ ð™£ð™ªð™¢ð™—ð™šð™§ ð™¤ð™› ð™¨ð™˜ð™–ð™¢ð™¨ ð™– ð™¡ð™–ð™£ð™œð™ªð™–ð™œð™š ð™¢ð™¤ð™™ð™š6ð™¡ ð™˜ð™–ð™£ ð™œð™šð™£ð™šð™§ð™–ð™©ð™š ð™–ð™© ð™¤ð™£ð™˜ð™š, ð™¬ð™ð™žð™˜ð™ ð™žð™¨ ð™¤ð™—ð™«ð™žð™¤ð™ªð™¨ð™¡ð™® ð™¬ð™¤ð™§ð™§ð™®ð™žð™£ð™œ ð™¬ð™ð™šð™£ ð™®ð™¤ð™ª ð™˜ð™¤ð™£ð™¨ð™žð™™ð™šð™§ ð™ð™¤ð™¬ ð™›ð™–ð™¨ð™© ð™¡ð™–ð™£ð™œð™ªð™–ð™œð™š ð™¢ð™¤ð™™ð™šð™¡ð™¨ ð™˜ð™–ð™£ ð™œð™šð™£ð™šð™§ð™–ð™©ð™š ð™©ð™šð™­ð™©. ð™ð™ð™žð™¨ ð™¢ð™–ð™ ð™šð™¨ ð™˜ð™®ð™—ð™šð™§ð™–ð™©ð™©ð™–ð™˜ð™ ð™¨ ð™¨ð™ªð™˜ð™ ð™–ð™¨ ð™¥ð™ð™žð™¨ð™ð™žð™£ð™œ ð™šð™¢ð™–ð™žð™¡ð™¨ ð™¥ð™–ð™§ð™©ð™žð™˜ð™ªð™¡ð™–ð™§ð™¡ð™® ð™šð™–ð™¨ð™® ð™©ð™¤ ð™§ð™šð™¥ð™¡ð™žð™˜ð™–ð™©ð™š ð™¬ð™ð™šð™£ ð™¥ð™ªð™© ð™žð™£ ð™©ð™ð™š ð™ð™–ð™£ð™™ð™¨ ð™¤ð™› ð™šð™«ð™šð™£ ð™– ð™£ð™¤ð™«ð™žð™˜ð™š ð™˜ð™®ð™—ð™šð™§ð™˜ð™§ð™žð™¢ð™žð™£ð™–ð™¡.

ðŸ’  ð•„ð”¸ð•€â„• ð”»ð”¼ð• :- @RIYAL_NOBI

        """,
        reply_markup=keyboard)



@app.on_callback_query(filters.regex("help"))
def help_callback(client, callback_query):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="ðŸ’  ð™±ðšžðš¢ ð™±ðš˜ðš ð™°ðšžðšðš‘ ð™µðš›ðš˜ðš– ð™¾ðš ðš—ðšŽðš› ðŸ’ ", url="https://t.me/RIYAL_NOBI"),
            ],
            [
                InlineKeyboardButton(text="â¬…ï¸", callback_data="back"),
            ],
        ]
    )

    app.send_message(
        callback_query.message.chat.id,
        """
ðŸŒŸ ð™¸ðš ðšˆðš˜ðšž ð™½ðšŽðšŽðš ð™±ðš˜ðš ð™°ðšžðšðš‘ ðŸŒŸ
        """,
        reply_markup=keyboard
    )
@app.on_callback_query(filters.regex("back"))
def back_to_start_callback(client, callback_query):
    # Return to the "/start" command
    start_bot(client, callback_query.message)
    
@app.on_message(filters.command("admin"))
def admin(client, message):
    if message.from_user.username in owners:
        app.send_message(message.chat.id, """\
ðŸ’  ð™°ð™³ð™¼ð™¸ð™½ ð™²ð™¾ð™¼ð™¼ð™°ð™½ð™³ðš‚ ðŸ’ 

/addauth ðš„ðš‚ð™´ðšð™½ð™°ð™¼ð™´ (ð™µðš˜ðš› ð™°ðšðš ðš„ðšœðšŽðš›ðšœ) â‡
/rmauth ðš„ðš‚ð™´ðšð™½ð™°ð™¼ð™´ (ð™µðš˜ðš› ðšðšŽðš–ðš˜ðšŸðšŽ ðš„ðšœðšŽðš›ðšœ) â‡

ð™¿ðš„ðšƒ ðš„ðš‚ð™´ðšð™½ð™°ð™¼ð™´ ðš†ð™¸ðšƒð™·ð™¾ðš„ðšƒ @ 

/broadcast (ð™µðš˜ðš› ð™±ðš›ðš˜ðšŠðšðšŒðšŠðšœðš ð™¼ðšŽðšœðšœðšŠðšðšŽ ðšƒðš˜ ð™°ðš•ðš• ðš„ðšœðšŽðš›ðšœ) â‡

/authlist (ð™µðš˜ðš› ðš‚ðšŽðšŽ ð™°ðš•ðš• ð™°ðšžðšðš‘ðš˜ðš›ðš’ðš£ðšŽðš ðš„ðšœðšŽðš›ðšœ) â‡
""")


@app.on_message(filters.command("addauth"))
def add_authorized_user(client, message):
    if message.from_user.username in owners:
        user_to_add = message.text[len("/addauth "):].strip()
        if len(user_to_add) == 0:
            app.send_message(message.chat.id, "âš ï¸ ðš‚ðšŽðš—ðš ð™»ðš’ðš”ðšŽ ðšƒðš‘ðš’ðšœ: /addauth NewUserUsername")
        else:
            if user_to_add not in allowed_users:
                allowed_users.append(user_to_add)
                if collection.find_one({"telegram_username": user_to_add}) is None:
                    # Add the user to MongoDB collection
                    collection.insert_one({"telegram_username": user_to_add})
                app.send_message(message.chat.id, f"ðŸŒŸ ðš„ðšœðšŽðš› {user_to_add} ðš‘ðšŠðšœ ðš‹ðšŽðšŽðš— ðšŠðšžðšðš‘ðš˜ðš›ðš’ðš£ðšŽðš ðšðš˜ ðšžðšœðšŽ ðšðš‘ðš’ðšœ ðš‹ðš˜ðš.")
            else:
                app.send_message(message.chat.id, f"ðŸ” ðš„ðšœðšŽðš› {user_to_add} ðš’ðšœ ðšŠðš•ðš›ðšŽðšŠðšðš¢ ðšŠðšžðšðš‘ðš˜ðš›ðš’ðš£ðšŽðš.")
    else:
        app.send_message(message.chat.id, "âŒ ðš‚ðš˜ðš›ðš›ðš¢, ðš¢ðš˜ðšž ðšŠðš›ðšŽ ðš—ðš˜ðš ðšŠðš— ðš˜ðš ðš—ðšŽðš› ðšðš˜ ðšžðšœðšŽ ðšðš‘ðšŽ ðšŒðš˜ðš–ðš–ðšŠðš—ðš /alive use alive check")

@app.on_message(filters.command("rmauth"))
def remove_authorized_user(client, message):
    if message.from_user.username in owners:
        user_to_remove = message.text[len("/rmauth "):].strip()
        if len(user_to_remove) == 0:
            app.send_message(message.chat.id, "âš  ðš‚ðšŽðš—ðš ð™»ðš’ðš”ðšŽ ðšƒðš‘ðš’ðšœ: /rmauth UserToRemoveUsername")
        else:
            if user_to_remove in allowed_users:
                allowed_users.remove(user_to_remove)
                # Remove the user from the MongoDB collection if it exists
                collection.delete_one({"telegram_username": user_to_remove})
                app.send_message(message.chat.id, f"ðŸš« ðš„ðšœðšŽðš› {user_to_remove} ðš‘ðšŠðšœ ðš‹ðšŽðšŽðš— ðš›ðšŽðš–ðš˜ðšŸðšŽðš ðšðš›ðš˜ðš– ðšŠðšžðšðš‘ðš˜ðš›ðš’ðš£ðšŽðš ðšžðšœðšŽðš›ðšœ.")
            else:
                app.send_message(message.chat.id, f"âš ï¸ ðš„ðšœðšŽðš› {user_to_remove} ðš’ðšœ ðš—ðš˜ðš ðš’ðš— ðšðš‘ðšŽ ðš•ðš’ðšœðš ðš˜ðš ðšŠðšžðšðš‘ðš˜ðš›ðš’ðš£ðšŽðš ðšžðšœðšŽðš›ðšœ.")

# All auth lists users -----
@app.on_message(filters.command("authlist") & filters.user(owners))
def list_authorized_users(client, message):
    if message.from_user.username in owners:
        user_list = "\nðŸ’  Verified @".join(allowed_users)
        app.send_message(message.chat.id, f"ðŸ’  ð™»ðš’ðšœðš ð™¾ðš ð™°ðš•ðš• ð™°ðšžðšðš‘ðš˜ðš›ðš’ðš£ðšŽðš ðš„ðšœðšŽðš›ðšœ ðŸ’  :\nâ„ All Active Users â„ \nâœ… Verified List âœ… \nðŸ’  Verified @{user_list}")



# Broadcast message to all users
def broadcast_message(message_text):
    for user in allowed_users:
        try:
            app.send_message(user, message_text)
        except Exception as e:
            print(f"âŒ ð™µðšŠðš’ðš•ðšŽðš ðšðš˜ ðšœðšŽðš—ðš ðšðš‘ðšŽ ðš‹ðš›ðš˜ðšŠðšðšŒðšŠðšœðš ðš–ðšŽðšœðšœðšŠðšðšŽ ðš?? {user}. Error: {str(e)}")

# Handle '/broadcast' command (for owners)
@app.on_message(filters.command("broadcast") & filters.user(owners))
def broadcast_message_command(client, message):
    # Check if the message has a text following the command
    if len(message.command) < 2:
        app.send_message(
            message.chat.id,
            "ðŸ“¤ ðš‚ðšŽðš—ðš ðšŠ ðš–ðšŽðšœðšœðšŠðšðšŽ ðšðš˜ ðš‹ðšŽ ðš‹ðš›ðš˜ðšŠðšðšŒðšŠðšœðšðšŽðš ðšŠðšœ ðšŠ ðš›ðšŽðš™ðš•ðš¢ ðšðš˜ ðšðš‘ðšŽ /broadcast ðšŒðš˜ðš–ðš–ðšŠðš—ðš.",
        )
    else:
        # Extract the message to be broadcasted
        broadcast_text = message.text.split(" ", 1)[1]

        broadcast_message(broadcast_text)

# Update 'allowed_users' list from the MongoDB collection
for user in collection.find({}):
    allowed_users.append(user['telegram_username'])

@app.on_message(filters.command("alive"))
def get_uptime(client, message):
    uptime_seconds = get_server_uptime()
    uptime_str = str(datetime.timedelta(seconds=uptime_seconds))
    total_cpu = get_total_cpu_usage()
    current_cpu = get_bot_cpu_usage()
    bot_alive_time = str(datetime.datetime.now() - bot_start_time)  # Calculate bot's uptime using bot_start_time

    alive_message = (
        f"âœ… Server Uptime: {uptime_str}\n"
        f"âœ… Total CPU Usage: {total_cpu:.2f}%\n"
        f"âœ… Current Bot CPU Usage: {current_cpu:.2f}%\n"
        f"âœ… Bot Alive Time: {bot_alive_time}"
    )

    app.send_message(message.chat.id, alive_message)
@app.on_message(filters.text)
def send_answer(client, message):
    if message.from_user.username in allowed_users:
        app.send_message(message.chat.id, get_response(message.text))
    else:
        app.send_message(message.chat.id, "âŒ ðš‚ðš˜ðš›ðš›ðš¢, ðš¢ðš˜ðšž ðšŠðš›ðšŽ ðš—ðš˜ðš ðšŠðšžðšðš‘ðš˜ðš›ðš’ðš£ðšŽðš ðšðš˜ ðš‹ðš˜ðš \nðŸŒŸ ð™±ðšžðš¢ ð™±ðš˜ðš ð™µðš›ðš˜ðš– @NOBINO_WORM_GPT_AI")

@app.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id ==DEVIL:
        fwded_mesg = await message.forward(chat_id=DEVIL, disable_notification=True)
        
print(f"NOBINO Worm Gpt BOT Is Active Now âœ…")      
app.run()
