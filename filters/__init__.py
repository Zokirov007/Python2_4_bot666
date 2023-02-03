from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from . guruh_uchun import guruh
from . kanal_uchun import kanal
from . shaxsiy_uchun import shaxsiy

if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(guruh)
    dp.filters_factory.bind(kanal)
    dp.filters_factory.bind(shaxsiy)
    pass
