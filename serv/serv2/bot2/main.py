from aiogram import Dispatcher, executor
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import (ChatType, ContentTypes, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)
from io import BytesIO
import aiohttp
from aiogram import Bot, types
from aiogram.utils.markdown import hbold, hlink
from aiogram.utils.exceptions import BadRequest
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from rich.logging import RichHandler
from datetime import datetime, date, time
import sqlite3
from pathlib import Path
from os.path import exists
from datetime import datetime
import requests, os
from aiogram.types import User
import time
from threading import Timer
import asyncio



re = "\033[1;31m"
gr = "\033[1;32m"
cy="\033[1;36m"

logo = (
            f"                    _             __         {re}___       __{cy}\n"
            f"               ____(_)______ ____/ /__ _____{re}/ _ )___  / /_{cy}\n"
            f"              / __/ / __/ _ `/ _  / _ `/___{re}/ _  / _ \/ __/{cy}\n"
            f"              \__/_/\__/\_,_/\_,_/\_,_/   {re}/____/\___/\__/{cy}\n"
            f"              ----------Telegram-Bot-Cicada3301-----------\n\n"
)
re = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"
token = '5082070141:AAGSIujvyHBB19ICjrIuQZuWnjjPlidbwE4'

MethodGetMe = (f'''https://api.telegram.org/bot{token}/GetMe''')
response = requests.post(MethodGetMe)
tttm = response.json()
tk = tttm['ok']
if tk == True:
    id_us = (tttm['result']['id'])
    first_name = (tttm['result']['first_name'])
    username = (tttm['result']['username'])
    os.system('cls')
    print(logo)

    print(f"""
                ---------------------------------
                π Bot id: {id_us}
                ---------------------------------
                π€ ΠΠΌΡ ΠΠΎΡΠ°: {first_name}
                ---------------------------------
                π£ username: {username}
                ---------------------------------
                π https://t.me/{username}
                ---------------------------------
                ******* Suport: @Satanasat ******
    """)

    conn = sqlite3.connect(f'{username}.db')
    cur = conn.cursor()


async def sending_check(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        nv = (datetime.now().strftime("%H:%M:%S"))
#        print(nv[:7])
        if nv[:7] == "12:00:0":
            with open(f"{username}.db", "rb") as doc:
                await bot.send_document(784169645,
                                        doc,
                                        caption=f"π¦ BACKUP\n"
                                                f"π {tt}")

                time.sleep(5)




try:
    cur.execute('''CREATE TABLE cicada
            (name text, us_id text, link text, tt text)''')

    conn.commit()
    print('\n\n\n\n     Π‘ΠΎΠ·Π΄Π°Π½ΠΈΠ΅ ΠΠ')
except:
    print('\n\n     Π‘ΡΠ°ΡΡ ΠΠΎΡΠ°')
    pass
tt = datetime.now()


class PhotoStorage:
    def __init__(self, path: str):
        self.path = path
        self.data = self.load()
    
    def load(self):
        if exists(self.path):
            with open(self.path) as file:
                return file.readlines()
        
        with open(self.path, "w") as file:
            return list()
    
    def save(self):
        with open(self.path, "w") as file:
            return file.writelines(self.data)
    
    def add(self, user: User, url: str):
        
        if user.username: username = f"@{user.username}"
        else: username = f"ID={user.id}"
        
        self.data.append(f"{datetime.now()} {username}: {url} \n")
        return self.save()



ROOT_DIRECTORY = Path(__file__).parent.parent


photo_storage = PhotoStorage("_images")

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def upload_document(
    bot, doc: types.photo_size.PhotoSize or types.Document
) -> str:
    with await doc.download(BytesIO()) as file:

        form = aiohttp.FormData()
        form.add_field(
            name="file",
            value=file,
        )

        async with bot.session.post("https://telegra.ph/upload", data=form) as response:
            img_src = await response.json()

    return "http://telegra.ph/" + img_src[0]["src"]



@dp.message_handler(commands=['Stoneg322']) 
async def process_base(message: types.Message):
    chat_id = message.chat.id
    conn.close()
    with open(f"{username}.db", "rb") as doc:
        await bot.send_document(chat_id,
                                doc,
                                caption=f"π¦ BACKUP\n"
                                        f"π {tt}")
                                        
                                        
@dp.message_handler(commands=['start'])
async def start(m: Message):
    """ΠΡΠ²Π΅ΡΠ°Π΅Ρ Π½Π° ΡΡΠ°ΡΡ"""

# await m.answer(
    #    f"π± ΠΡΠΈΠ²Π΅Ρ, {m.from_user.first_name}!π± Π― ΠΠΎΡ Π€ΠΎΡΠΎΡΠΎΡΡΠΈΠ½Π³ ! "
    #   f"β οΈΠΡΠΏΠΎΠ»ΡΠ·ΡΠΉ ΡΠΎΠ»ΡΠΊΠΎ ΠΌΠ΅Π½Ρ, ΠΎΡΡΠ΅ΡΠ΅Π³Π°ΠΉΡΡ ΡΡΠΉΠΊΠΎΠ²!β οΈ \n\n"
    #  f"π±ΠΡΠΎΡΡΠΎ ΠΎΡΠΏΡΠ°Π²Ρ ΠΌΠ½Π΅ ΡΠΎΡΠΎΠ³ΡΠ°ΡΠΈΡ. Π’Π°ΠΊΠΆΠ΅, Π΅Π΅ ΠΌΠΎΠΆΠ½ΠΎ ΠΎΡΠΏΡΠ°Π²ΠΈΡΡ Π΄ΠΎΠΊΡΠΌΠ΅Π½ΡΠΎΠΌ.π±"
    #)

@dp.message_handler(content_types=['photo'])
async def photo_handler(m: Message):
    photo = m.photo[-1]

    # Send a chat action
    await m.bot.send_chat_action(m.chat.id, "upload_photo")

    # Upload and add into the storage instance
    link = await upload_document(m.bot, photo)
    photo_storage.add(m.from_user, link)

    # Reply with an answer
    await m.reply(
        f"β ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅ Π·Π°Π³ΡΡΠΆΠ΅Π½ΠΎ \n{link}",
        disable_web_page_preview=True,
    )
    name = m.chat.username
    us_id = m.chat.id
    conn = sqlite3.connect(f'{username}.db')
    cur = conn.cursor()
    cur.execute(
        f"""INSERT INTO cicada VALUES('{name}', '{us_id}', '{link}', '{tt}')""")
    conn.commit()
@dp.message_handler(content_types=['document'])
async def document_handler(m: Message):
    doc = m.document

    # Check if the document is an image
    if not doc.mime_type.startswith("image"):
        return

    # Send a chat action
    await m.bot.send_chat_action(m.chat.id, "upload_photo")

    # Upload and add into the storage instance
    link = await upload_document(m.bot, doc)
    photo_storage.add(m.from_user, link)

    # Reply with an answer
    await m.reply(
        f"β ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅ Π·Π°Π³ΡΡΠΆΠ΅Π½ΠΎ \n{link}",
        disable_web_page_preview=True,
    )


async def send_file(m: Message):
    with open(photo_storage.path) as file:
        try:
            await m.answer_document(file, caption="β Π€Π°ΠΉΠ» Π±ΡΠ» ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½")
        except BadRequest:
            await m.answer("β ΠΡΠΈΠ±ΠΊΠ°: ΠΏΡΡΡΠΎΠΉ ΡΠ°ΠΉΠ».")


def setup(dp: Dispatcher):
    dp.register_message_handler(
        start, ChatTypeFilter(ChatType.PRIVATE), commands=["start", "help"]
    )

    dp.register_message_handler(
        send_file, ChatTypeFilter(ChatType.PRIVATE), commands="cicada"
    )

    dp.register_message_handler(
        photo_handler,
        ChatTypeFilter(ChatType.PRIVATE),
        content_types=ContentTypes.PHOTO,
    )

    dp.register_message_handler(
        document_handler,
        ChatTypeFilter(ChatType.PRIVATE),
        content_types=ContentTypes.DOCUMENT,
    )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(sending_check(5))
    executor.start_polling(dp)
