1| # Credit @RushikeshNarule777.
2| # Please Don't remove credit.
3| # Born to make history @RushikeshNarule777 !
4| # Thank you RushikeshNarule777 for helping us in this Journey
5| # 🥰  Thank you for giving me credit @RushikeshNarule777  🥰
6| # for any error please contact me -> telegram@RushikeshNarule777 or insta @RushikeshNarule777 
7| # rip paid developers 🤣 - >> No need to buy paid source code while @RushikeshNarule777 is here 😍😍
8| import logging
9| from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid
10| from info import *
11| from imdb import IMDb
12| import asyncio
13| from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
14| from pyrogram import enums
15| from typing import Union
16| import re
17| import os
18| from datetime import datetime
19| from typing import List
20| from database.users_chats_db import db
21| from bs4 import BeautifulSoup
22| import requests
23| import aiohttp
24| from shortzy import Shortzy
25| 
26| logger = logging.getLogger(__name__)
27| logger.setLevel(logging.INFO)
28| 
29| BTN_URL_REGEX = re.compile(
30|     r"(\[([^\[]* ▋
