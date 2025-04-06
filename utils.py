# Credit @RushikeshNarule777.
# Please Don't remove credit.
# Born to make history @RushikeshNarule777 !
# Thank you RushikeshNarule777 for helping us in this Journey
# 🥰  Thank you for giving me credit @RushikeshNarule777  🥰
# for any error please contact me -> telegram@RushikeshNarule777 or insta @RushikeshNarule777 
# rip paid developers 🤣 - >> No need to buy paid source code while @RushikeshNarule777 is here 😍😍
import logging
from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid
from info import *
from imdb import IMDb
import asyncio
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import enums
from typing import Union
import re
import os
from datetime import datetime
from typing import List
from database.users_chats_db import db
from bs4 import BeautifulSoup
import requests
import aiohttp
from shortzy import Shortzy
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

 BTN_URL_REGEX = re.compile(
30|     r"(\[([^\[]*)\]\((.*?)\))"
