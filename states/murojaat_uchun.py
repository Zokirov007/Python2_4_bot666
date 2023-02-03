from aiogram.dispatcher.filters.state import State,StatesGroup

class Forma(StatesGroup):
    ism_qabul_qilish_holati = State()
    fam_qabul_qilish_holati = State()
    yosh_qabul_qilish_holati = State()
    tel_qabul_qilish_holati = State()
    msg_qabul_qilish_holati = State()
    tasdiqlash_holati = State()

class Forma1(StatesGroup):
    ism1_qabul_qilish_holati = State()
    fam1_qabul_qilish_holati = State()
    yosh1_qabul_qilish_holati = State()
    tel1_qabul_qilish_holati = State()
    msg1_qabul_qilish_holati = State()
    tasdiqlash1_holati = State()