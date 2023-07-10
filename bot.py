from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TG_TOKEN

from downloader import VideoDownloader

API_TOKEN = TG_TOKEN
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    await message.reply("Hello, bro")


@dp.message_handler()
async def download_video(message: Message):
    yt = VideoDownloader(message.text)
    video_title = yt._yt.title
    yt.download_video()
    with open(f'downloads/{video_title}.mp4', 'rb') as video:
        await message.answer_video(video)
