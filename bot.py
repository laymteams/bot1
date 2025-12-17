import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InputMediaPhoto
)
from aiogram.filters import Command

# 🔑 ТОКЕН БОТА
BOT_TOKEN = "8468276373:AAEz6wOgj6JvMnnYp8zVEmxpeqrU5r5Q14A"

# 📦 КОНФИГИ ДЛЯ КАЖДОГО ПОЛЬЗОВАТЕЛЯ
USER_CONFIGS = {
    #5445296130: "vless://b1a583a0-d9d3-4bdf-915e-6bf9cc061429@144.31.252.107:443?type=grpc&encryption=none&serviceName=&authority=&security=reality&pbk=_cxXv_IKij5XbeAsqEJvRHg-AmjO9A_fT4zeMxrk5CY&fp=chrome&sni=google.com&sid=65&spx=%2F#%D0%9C%D0%BE%D0%B8%20%D0%BF%D0%BE%D0%B4%D0%BE%D0%BF%D0%B5%D1%87%D0%BD%D1%8B%D0%B5%20%D0%B2%D0%BF%D0%BD%D1%89%D0%B8%D0%BA%D0%B8)))-%40laymicus",
    6557932472: "vless://597aa492-a860-4729-a93f-f700d378d37e@144.31.252.107:443?type=grpc&encryption=none&serviceName=&authority=&security=reality&pbk=_cxXv_IKij5XbeAsqEJvRHg-AmjO9A_fT4zeMxrk5CY&fp=chrome&sni=google.com&sid=65&spx=%2F#%D0%9C%D0%BE%D0%B8%20%D0%BF%D0%BE%D0%B4%D0%BE%D0%BF%D0%B5%D1%87%D0%BD%D1%8B%D0%B5%20%D0%B2%D0%BF%D0%BD%D1%89%D0%B8%D0%BA%D0%B8)))-%40qqcascoqq",
    8064069403: "vless://ff965144-10e9-4951-9f6a-be44154a120d@144.31.252.107:443?type=grpc&encryption=none&serviceName=&authority=&security=reality&pbk=_cxXv_IKij5XbeAsqEJvRHg-AmjO9A_fT4zeMxrk5CY&fp=chrome&sni=google.com&sid=65&spx=%2F#%D0%9C%D0%BE%D0%B8%20%D0%BF%D0%BE%D0%B4%D0%BE%D0%BF%D0%B5%D1%87%D0%BD%D1%8B%D0%B5%20%D0%B2%D0%BF%D0%BD%D1%89%D0%B8%D0%BA%D0%B8)))-%40Mementoquodmorieris",
}

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📥 Получить конфигурацию", callback_data="get_config")]
    ]
)

@dp.message(Command("start"))
async def start(message: Message):
    if message.from_user.id not in USER_CONFIGS:
        return await message.answer("❌ Для вас конфигурация не найдена")

    await message.answer(
        "Нажмите кнопку ниже, чтобы получить конфигурацию 👇",
        reply_markup=keyboard
    )

@dp.callback_query(F.data == "get_config")
async def send_config(callback: CallbackQuery):
    user_id = callback.from_user.id

    if user_id not in USER_CONFIGS:
        return await callback.answer("Конфигурация не найдена", show_alert=True)

    config_text = USER_CONFIGS[user_id]

    # 1️⃣ Конфиг
    await callback.message.answer(
        f"📄 **Ваша конфигурация:**\n\n```{config_text}```",
        parse_mode="Markdown"
    )

    # 2️⃣ Инструкция + скрины
    media = [
        InputMediaPhoto(
            media=open("screen1.jpg", "rb"),
            caption=(
                "📲 **Инструкция**\n\n"
                "Скачиваем **v2RayTun**\n\n"
                "❗ У кого был Happ — НЕ удаляем\n"
                "❗ У кого была старая подписка — удаляем (чек скрин 1,2)\n\n"
                "Google Play:\n"
                "https://play.google.com/store/apps/details?id=com.v2raytun.android&hl=ru\n\n"
                "App Store:\n"
                "https://apps.apple.com/app/id6476628951\n\n"
                "После установки копируем конфиг (сообщение выше)\n"
                "и вставляем его (чек скрин 3,4)\n\n"
                "✅ ВСЁ!"
            )
        ),
        InputMediaPhoto(media=open("screen2.jpg", "rb")),
        InputMediaPhoto(media=open("screen3.jpg", "rb")),
        InputMediaPhoto(media=open("screen4.jpg", "rb")),
    ]

    await bot.send_media_group(
        chat_id=callback.message.chat.id,
        media=media
    )

    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
