import telebot

from django.conf import settings


bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)


def send_application_to_telegram(message):
    from .models import Telegram

    try:
        for profile in Telegram.objects.all():
            if profile is not None:
                bot.send_message(profile.chat_id, message)
    except telebot.apihelper.ApiTelegramException:
        return f'Chat not found!'
