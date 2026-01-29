from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import re
import os
import uuid

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text(
        "🧮 Inline Calculator Bot Ready!\n\n"
        "যেকোনো চ্যাটে লিখুন:\n"
        "@YourBotUsername 5+5"
    )

def inline_calc(update, context):
    query = update.inline_query.query.strip()

    if not query:
        return

    if not re.match(r'^[0-9+\-*/(). ]+$', query):
        result = "❌ Invalid expression"
    else:
        try:
            result = str(eval(query))
        except:
            result = "❌ Error"

    article = InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        title=f"Result: {result}",
        input_message_content=InputTextMessageContent(
            f"🧮 {query} = {result}"
        )
    )

    update.inline_query.answer([article], cache_time=1)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(InlineQueryHandler(inline_calc))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
