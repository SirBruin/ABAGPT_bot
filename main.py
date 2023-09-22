# import required lib
import logging
import re

from GPT_conf import GPT
from typing import Final
from joke_conf import *
from translator import translation

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters
)

# Bot data
__BOT_Token: Final = "Your Bot Token"
Developer_ID = ["Your id"]

# config & setup logging format
logging.basicConfig(format='%(levelname)s - (%(asctime)s) - %(message)s - (Line: %(lineno)d) - [%(filename)s]',
                    datefmt='%H:%M:%S',
                    encoding='utf-8',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

WHAT, TARGET, TEXTS, TRANSLATE, CHAT, JOKE = range(6)

# markup bottom
start_markup_keyboard = ReplyKeyboardMarkup(
    keyboard=[["Chat GPT", "Joke"],
              ["Help", "Translate"]],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder=" what do you want ? ",
)


# set handlers
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    logger.info("user %s whit name ~%s~ start bot whit ~%s~ id.", update.effective_user.username,
                update.effective_user.full_name, update.effective_user.id)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""
Hi every one 
welcome to ABAGPT Bot 
if you want help? /help
""",
        reply_to_message_id=update.effective_message.id,
        reply_markup=start_markup_keyboard
    )
    return WHAT


async def first_language_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("user %s whit name ~%s~ whit ~%s~ id  select language mode.", update.effective_user.username,
                update.effective_user.full_name, update.effective_user.id)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Please Enter Your Language ? \n if you cancel step ? /cancel',
        reply_to_message_id=update.effective_message.id,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[['English', 'Persian', 'French', 'Arabic'],
                      ['Spanish', 'Korean', 'Germany', 'Hindi'],
                      ['Armeny', 'Italy', 'Japany', 'Romani'],
                      ['Russian', 'Serbian', 'Turkish', 'Ukrainy'],
                      ['Chinese', 'Canada', ],
                      ['/cancel']],
            one_time_keyboard=True,
            input_field_placeholder='your language ? '
        )
    )
    return TARGET


async def target_language_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_message.text.lower() == 'english':
        context.user_data['first_language'] = 'en'
    if update.effective_message.text.lower() == 'persian':
        context.user_data['first_language'] = 'fa'
    if update.effective_message.text.lower() == 'french':
        context.user_data['first_language'] = 'fr'
    if update.effective_message.text.lower() == 'spanish':
        context.user_data['first_language'] = 'es'
    if update.effective_message.text.lower() == 'arabic':
        context.user_data['first_language'] = 'ar'
    if update.effective_message.text.lower() == 'korean':
        context.user_data['first_language'] = 'ko'
    if update.effective_message.text.lower() == 'germany':
        context.user_data['first_language'] = 'de'
    if update.effective_message.text.lower() == 'hindi':
        context.user_data['first_language'] = 'hi'
    if update.effective_message.text.lower() == 'armeny':
        context.user_data['first_language'] = 'hy'
    if update.effective_message.text.lower() == 'italy':
        context.user_data['first_language'] = 'it'
    if update.effective_message.text.lower() == 'japany':
        context.user_data['first_language'] = 'ja'
    if update.effective_message.text.lower() == 'romani':
        context.user_data['first_language'] = 'ro'
    if update.effective_message.text.lower() == 'russian':
        context.user_data['first_language'] = 'ru'
    if update.effective_message.text.lower() == 'serbian':
        context.user_data['first_language'] = 'sr-SP'
    if update.effective_message.text.lower() == 'turkish':
        context.user_data['first_language'] = 'tr'
    if update.effective_message.text.lower() == 'ukrainy':
        context.user_data['first_language'] = 'uk'
    if update.effective_message.text.lower() == 'chinese':
        context.user_data['first_language'] = 'zh-CN'
    if update.effective_message.text.lower() == 'canada':
        context.user_data['first_language'] = 'ca'
    logger.info("user %s whit name ~%s~ whit ~%s~ id  select %s first language .", update.effective_user.username,
                update.effective_user.full_name, update.effective_user.id, update.effective_message.text)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Please Enter Your text Language for translate your text ? \n if you cancel step ? /cancel',
        reply_to_message_id=update.effective_message.id,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[['English', 'Persian', 'French', 'Arabic'],
                      ['Spanish', 'Korean', 'Germany', 'Hindi'],
                      ['Armeny', 'Italy', 'Japany', 'Romani'],
                      ['Russian', 'Serbian', 'Turkish', 'Ukrainy'],
                      ['Chinese', 'Canada', ],
                      ['/cancel']],
            one_time_keyboard=True,
            input_field_placeholder='your text language ? '
        )
    )
    return TEXTS


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_message.text.lower() == 'english':
        context.user_data['target_language'] = 'en'
    if update.effective_message.text.lower() == 'persian':
        context.user_data['target_language'] = 'fa'
    if update.effective_message.text.lower() == 'french':
        context.user_data['target_language'] = 'fr'
    if update.effective_message.text.lower() == 'spanish':
        context.user_data['target_language'] = 'es'
    if update.effective_message.text.lower() == 'arabic':
        context.user_data['target_language'] = 'ar'
    if update.effective_message.text.lower() == 'korean':
        context.user_data['target_language'] = 'ko'
    if update.effective_message.text.lower() == 'germany':
        context.user_data['target_language'] = 'de'
    if update.effective_message.text.lower() == 'hindi':
        context.user_data['target_language'] = 'hi'
    if update.effective_message.text.lower() == 'armeny':
        context.user_data['target_language'] = 'hy'
    if update.effective_message.text.lower() == 'italy':
        context.user_data['target_language'] = 'it'
    if update.effective_message.text.lower() == 'japany':
        context.user_data['target_language'] = 'ja'
    if update.effective_message.text.lower() == 'romani':
        context.user_data['target_language'] = 'ro'
    if update.effective_message.text.lower() == 'russian':
        context.user_data['target_language'] = 'ru'
    if update.effective_message.text.lower() == 'serbian':
        context.user_data['target_language'] = 'sr-SP'
    if update.effective_message.text.lower() == 'turkish':
        context.user_data['target_language'] = 'tr'
    if update.effective_message.text.lower() == 'ukrainy':
        context.user_data['target_language'] = 'uk'
    if update.effective_message.text.lower() == 'chinese':
        context.user_data['target_language'] = 'zh-CN'
    if update.effective_message.text.lower() == 'canada':
        context.user_data['target_language'] = 'ca'
    context.user_data['trg'] = update.effective_message.text
    logger.info("user %s whit name ~%s~ whit ~%s~ id  select %s target language.", update.effective_user.username,
                update.effective_user.full_name, update.effective_user.id, update.effective_message.text)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Please Enter Your text for translate ? \n if you cancel step ? /cancel',
        reply_to_message_id=update.effective_message.id,
        reply_markup=ReplyKeyboardRemove()
    )
    return TRANSLATE


async def translate_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['text'] = update.effective_message.text
    logger.info("user %s whit name ~%s~ whit ~%s~ id  select %s text.", update.effective_user.username,
                update.effective_user.full_name, update.effective_user.id, update.effective_message.text)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'your text to translate {context.user_data["trg"]} language \n\n '
             f'{translation(context.user_data["text"], context.user_data["first_language"], context.user_data["target_language"])}',
        reply_to_message_id=update.effective_message.id,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[['/start', '/cancel']],
            resize_keyboard=True,
            one_time_keyboard=True,
            input_field_placeholder=' ? '
        )
    )
    return WHAT


async def gpt_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("user %s whit name ~%s~ whit ~%s~ id  select gpt mode.", update.effective_user.username,
                update.effective_user.full_name, update.effective_user.id)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Please Enter Your Question ? ',
        reply_to_message_id=update.effective_message.id,
        reply_markup=ReplyKeyboardRemove()
    )
    return CHAT


async def response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'please wait... ',
        reply_to_message_id=update.effective_message.id,
        reply_markup=ReplyKeyboardRemove()
    )
    user_question = update.effective_message.text
    answer = GPT(user_question)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'answer to "{update.effective_user.full_name}" by question : {user_question} ? \n\n '
             f'{answer.gpt_response()} ',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[['/start', '/cancel']],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    return WHAT


async def joke_language_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("user %s whit name ~%s~ whit ~%s~ id  select %s joke language.", update.effective_user.username,
                update.effective_user.full_name, update.effective_user.id, update.effective_message.text)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Please Enter Your Language ? \n if you cancel step ? /cancel',
        reply_to_message_id=update.effective_message.id,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[['English', 'Persian'],
                      ['/cancel']],
            resize_keyboard=True,
            one_time_keyboard=True,
            input_field_placeholder='your language ? '
        )
    )
    return JOKE


async def joke_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_language = update.effective_message.text
    if user_language == "Persian":
        context.user_data['language'] = 'fa'
    if user_language == "English":
        context.user_data['language'] = 'en'
    logger.info("user %s whit name ~%s~ whit ~%s~ id select joke mode.", update.effective_user.username,
                update.effective_user.full_name, update.effective_user.id)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=jok(context.user_data['language']),
        reply_to_message_id=update.effective_message.message_id,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[['/start']],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    return WHAT


async def joke_command_handler(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    user_language = job.data['lang']
    if user_language == "Persian":
        job.data['lang'] = 'fa'
    if user_language == "English":
        job.data['lang'] = 'en'
    logger.info("user  whit ~%s~ id select joke command.", job.user_id)
    await context.bot.send_message(
        chat_id=job.chat_id,
        text=jok(job.data['lang']),
    )

    return WHAT


async def set_joke_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        due = float(context.args[0])
        lang = str(context.args[1])
        job_name = str(update.effective_user.id)
        if due < 7:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Please set an interval greater or equal than 7."
            )
            return
        job_removed = remove_job_if_exists(job_name, context, lang)
        context.job_queue.run_repeating(
            joke_command_handler,
            chat_id=update.effective_chat.id,
            interval=due,
            name=job_name,
            data={
                "lang": lang,
                "due": due
            }
        )
        text = "Your joke Job was Created"
        if job_removed:
            text += "\nAll your jobs were deleted."
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text
        )
    except (IndexError, ValueError):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="You set my job wrong."
        )


async def unset_joke_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        jobs = context.job_queue.get_jobs_by_name(str(update.effective_user.id))
        lang = str(context.args[0])
        for job in jobs:
            if job.data["lang"] == lang:
                job.schedule_removal()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Your joke jobs are all deleted."
        )
    except (IndexError, ValueError):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="You set my job wrong."
        )


def remove_job_if_exists(name: str, context: ContextTypes.DEFAULT_TYPE, lang: str):
    all_jobs = context.job_queue.get_jobs_by_name(name)
    if not all_jobs:
        return False
    for job in all_jobs:
        if job.data["lang"] == lang:
            job.schedule_removal()
    return True


async def gpt_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = " ".join(context.args)
    answer = GPT(user_question)
    if update.effective_chat.type == 'group':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'answer to "{update.effective_user.full_name}" by question : {user_question} ? \n\n {answer.gpt_response()}',
            reply_to_message_id=update.effective_message.id,
        )
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'answer to "{update.effective_user.full_name}" by question : {user_question} ? \n\n {answer.gpt_response()}',
        reply_to_message_id=update.effective_message.id,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[['/start']],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )


async def notfound_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='your command not found <>',
        reply_to_message_id=update.effective_message.id
    )


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("User ~%s~ need help & press help command whit %s~ id.", update.effective_user.full_name,
                update.effective_user.id)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""
Bot Commands :
/start -> started bot
/gpt <QUESTION>  -> Asking questions from chat GPT Ai
/joke <due> <language> -> return a funny persian joke in your set time in <due>
/joke_delete <language> -> delete joke job and stop joke job
**note** in joke command if you run command in per second after language set time for example /joke <language> <time> 
**note** supported language -> persian : فارسی  , english : انگلیسی
    """,
        reply_to_message_id=update.effective_message.id
    )
    return WHAT


async def cancel_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    logger.info("user %s whit name ~%s~ whit ~%s~ id cancel option.", update.effective_user.username,
                update.effective_user.full_name, update.effective_user.id)
    await context.bot.send_message(
        chat_id=update.effective_user.id,
        text="Bye! I hope we can talk again some day.",
        reply_markup=ReplyKeyboardRemove(),
        reply_to_message_id=update.effective_message.id,
    )
    return ConversationHandler.END


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error('error is :  %s by user: %s', context.error,
                 update.effective_user.username)


if __name__ == "__main__":
    logger.warning("building bot ...")
    bot = ApplicationBuilder().token(__BOT_Token).build()

    GPT_filter = filters.Regex(re.compile(r'^(Chat GPT)$', re.IGNORECASE))
    joke_filter = filters.Regex(re.compile(r'^(Joke)$', re.IGNORECASE))
    help_filter = filters.Regex(re.compile(r'^(Help)$', re.IGNORECASE))
    lang_filter = filters.Regex(re.compile(r'^(English|Persian)$', re.IGNORECASE))
    translate_filter = filters.Regex(re.compile(r'^(Translate)$', re.IGNORECASE))
    language_filter = filters.Regex(re.compile(r'^(English|Persian|French|Arabic|Spanish|Korean|'
                                               r'Germany|Hindi|Armeny|Italy|Japany|Romani|'
                                               r'Russian|Serbian|Turkish|Ukrainy|Chinese|Canada)$', re.IGNORECASE))
    command_filter = filters.Regex(re.compile(r'^(~/start|~/help|~/joke|~Chat GPT|~/cancel)', re.IGNORECASE))
    # adding handlers
    bot.add_handler(CommandHandler('help', help_handler))
    bot.add_handler(MessageHandler(command_filter, notfound_handler))
    bot.add_handler(CommandHandler('joke', set_joke_command_handler))
    bot.add_handler(CommandHandler('joke_delete', unset_joke_command_handler))
    bot.add_handler(CommandHandler('gpt', gpt_command_handler))
    bot.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler("start", start_handler)
        ],
        states={
            WHAT: [
                MessageHandler(filters=GPT_filter, callback=gpt_handler),
                MessageHandler(filters=joke_filter, callback=joke_language_handler),
                MessageHandler(filters=help_filter, callback=help_handler),
                MessageHandler(filters=translate_filter, callback=first_language_handler)
            ],
            CHAT: [MessageHandler(filters=filters.TEXT, callback=response)],
            JOKE: [MessageHandler(filters=lang_filter, callback=joke_handler)],
            TARGET: [MessageHandler(filters=language_filter, callback=target_language_handler)],
            TEXTS: [MessageHandler(filters=language_filter, callback=text_handler)],
            TRANSLATE: [MessageHandler(filters=filters.TEXT, callback=translate_handler)]

        },
        fallbacks={
            CommandHandler('cancel', cancel_handler),
        },
        allow_reentry=True,

    )
    ),
    # error handler
    bot.add_error_handler(error_handler),

    # bot running
    bot.run_polling(allowed_updates=[Update.MESSAGE])

