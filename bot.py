import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

# =====================
# 🔧 FILL HERE (TO'LDIR)
# =====================
BOT_TOKEN = "8956510505:AAEhCCMDz46X9cl5YdNAgoEvjES--6f71wc"
ADMIN_ID =  8203205151

CARD_NUMBER = "9860350147021686"
CARD_OWNER = "B........SH....."
# =====================

orders = {}

PRODUCTS = {
    "55": ("💎 55 Diamond", "13 000 so'm"),
    "86": ("💎 86 Diamond", "17 000 so'm"),
    "165": ("💎 165 Diamond", "30 000 so'm"),
    "275": ("💎 275 Diamond", "48 000 so'm"),
    "565": ("💎 565 Diamond", "98 000 so'm"),
    "706": ("💎 706 Diamond", "125 000 so'm"),

    "uc60": ("🎯 PUBG UC 60", "13 000 so'm"),
    "uc120": ("🎯 PUBG UC 120", "25 000 so'm"),
    "uc180": ("🎯 PUBG UC 180", "35 000 so'm"),
    "uc325": ("🎯 PUBG UC 325", "60 000 so'm"),
}

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

def menu():
    kb = InlineKeyboardBuilder()

    for key, value in PRODUCTS.items():
        kb.button(text=value[0], callback_data=key)

    kb.adjust(1)
    return kb.as_markup()


@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        "💎 DONAT SHOP\nMahsulotni tanlang:",
        reply_markup=menu()
    )


@dp.callback_query()
async def buy(call: CallbackQuery):

    name, price = PRODUCTS[call.data]

    orders[call.from_user.id] = (name, price)

    await call.message.answer(
f"""
🧾 BUYURTMA

📦 {name}
💰 {price}

💳 Karta:
{CARD_NUMBER}

👤 {CARD_OWNER}

📌 Endi o'yin ID yuboring
"""
    )

    await call.answer()


@dp.message()
async def get_id(message: Message):

    if not message.text.isdigit():
        return

    game_id = message.text

    name, price = orders.get(
        message.from_user.id,
        ("Noma'lum", "Noma'lum")
    )

    await message.answer(
f"""
✅ Buyurtma qabul qilindi

📦 {name}
💰 {price}

🆔 ID: {game_id}

⏳ Tekshirilmoqda
"""
    )

    await bot.send_message(
        ADMIN_ID,
f"""
🆕 YANGI BUYURTMA

📦 Mahsulot: {name}
💰 Summa: {price}
🆔 ID: {game_id}

👤 User ID: {message.from_user.id}
👤 Username: @{message.from_user.username or "yo'q"}
"""
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
