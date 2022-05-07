import asyncio
from pyrogram import Client, filters
from pyrogram.errors import QueryIdInvalid, FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent

from configs import Config
from tool import SearchYTS, SearchAnime, Search1337x, SearchPirateBay
import os
import play_scraper
from pyrogram import Client, filters
from pyrogram.types import *



DEFAULT_SEARCH_MARKUP = [
                    [InlineKeyboardButton("𝗦𝗲𝗮𝗿𝗰𝗵 𝗬𝗧𝗦 𝗠𝗼𝘃𝗶𝗲𝘀 📺🔥", switch_inline_query_current_chat="YTS "),
                     InlineKeyboardButton("𝗦𝗲𝗮𝗿𝗰𝗵 𝗜𝗻 1337x 🔥", switch_inline_query_current_chat="")],
                    [InlineKeyboardButton("𝗦𝗲𝗮𝗿𝗰𝗵 𝗔𝗻𝘆 𝗧𝗼𝗿𝗿𝗲𝗻𝘁 𝗶𝗻 𝗣𝗶𝗿𝗮𝘁𝗲𝗯𝗮𝘆 ☠️🍁", switch_inline_query_current_chat="PB ")],
                    [InlineKeyboardButton("𝗝𝗼𝗶𝗻 𝗚𝗿𝗼𝘂𝗽 🌷 ", url="https://t.me/joinchat/bZfGkMGaGwswZjI1"),
                     InlineKeyboardButton("𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗠𝗲 🥰🌷", url="https://t.me/Ravindu_Deshanz")]
                ]


@Client.on_message(filters.command("sta"))
async def sta_handler(_, message: Message):
    try:
        await message.reply_sticker("CAACAgUAAxkBAAEC11VhMKoiYfFiHo9BxHHaD2M2rMIW0gACDgUAArD8gFX57AkpeFVIYiAE")
        await message.reply_text(
            text="𝗛𝗶...✨💐...𝗜 𝗮𝗺 𝗮 𝗣𝗼𝘄𝗲𝗿𝗳𝘂𝗹 𝗧𝗼𝗿𝗿𝗲𝗻𝘁 𝗦𝗲𝗮𝗿𝗰𝗵 𝗕𝗼𝘁 𝗶𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 🥰🔥\n\n"
                 "𝗠𝗮𝗱𝗲 𝗳𝗼𝗿 𝗣𝗮𝗻𝘁𝗵𝗲𝗿 𝗠𝗶𝗿𝗿𝗼𝗿 𝗚𝗿𝗼𝘂𝗽🥰✨\n\n"
                 "𝗬𝗧𝗦 , 𝗣𝗶𝗿𝗮𝘁𝗲𝗕𝗮𝘆 𝗮𝗻𝗱 13377𝘅 𝗔𝗿𝗲 𝗦𝘂𝗽𝗽𝗿𝘁𝗲𝗱 🔥\n\n"
                 "𝗟𝗶𝘃𝗲 𝗼𝗻 𝗛𝗲𝗿𝗼𝗸𝘂 𝗦𝗲𝗿𝘃𝗲𝗿 🔥\n\n"
                 "𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗯𝘆 @Ravindu_Deshanz ⚡️\n\n"
                 "𝗔𝗹𝗹 𝘁𝗵𝗲 𝗢𝗽𝘁𝗶𝗼𝗻𝘀 𝗔𝗿𝗲 𝗕𝗲𝗹𝗼𝘄 🌶🥰",
            disable_web_page_preview=True,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(DEFAULT_SEARCH_MARKUP)
        )
    except FloodWait as e:
        print(f"[{Config.SESSION_NAME}] - Sleeping for {e.x}s")
        await asyncio.sleep(e.x)
        await sta_handler(_, message)


@Client.on_inline_query()
async def inline_handlers(_, inline: InlineQuery):
    search_ts = inline.query
    answers = []
    if search_ts == "":
        answers.append(
            InlineQueryResultArticle(
                title="𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝘆𝗽𝗲 𝗮 𝗡𝗮𝗺𝗲 𝗮𝗻𝗱 𝗜 𝗰𝗮𝗻 𝗳𝗶𝗻𝗱 𝗶𝘁 🥰🔥",
                description="𝐒𝐞𝐚𝐫𝐜𝐡 𝐟𝐨𝐫 𝐓𝐨𝐫𝐫𝐞𝐧𝐭𝐬 𝐢𝐧 𝐚 𝐫𝐞𝐚𝐥𝐭𝐢𝐦𝐞 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 🔥",
                input_message_content=InputTextMessageContent(
                    message_text="𝗛𝗶...✨💐...𝗜 𝗮𝗺 𝗮 𝗣𝗼𝘄𝗲𝗿𝗳𝘂𝗹 𝗧𝗼𝗿𝗿𝗲𝗻𝘁 𝗦𝗲𝗮𝗿𝗰𝗵 𝗕𝗼𝘁 𝗶𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 🥰🔥\n\n"
                 "𝗠𝗮𝗱𝗲 𝗳𝗼𝗿 𝗣𝗮𝗻𝘁𝗵𝗲𝗿 𝗠𝗶𝗿𝗿𝗼𝗿 𝗚𝗿𝗼𝘂𝗽🥰✨\n\n"
                 "𝗬𝗧𝗦 , 𝗣𝗶𝗿𝗮𝘁𝗲𝗕𝗮𝘆 𝗮𝗻𝗱 13377𝘅 𝗔𝗿𝗲 𝗦𝘂𝗽𝗽𝗿𝘁𝗲𝗱 🔥\n\n"
                 "𝗟𝗶𝘃𝗲 𝗼𝗻 𝗛𝗲𝗿𝗼𝗸𝘂 𝗦𝗲𝗿𝘃𝗲𝗿 🔥\n\n"
                 "𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗯𝘆 @Ravindu_Deshanz ⚡️\n\n"
                 "𝗔𝗹𝗹 𝘁𝗵𝗲 𝗢𝗽𝘁𝗶𝗼𝗻𝘀 𝗔𝗿𝗲 𝗕𝗲𝗹𝗼𝘄 🌶🥰",
                    parse_mode="Markdown"
                ),
                reply_markup=InlineKeyboardMarkup(DEFAULT_SEARCH_MARKUP)
            )
        )
    elif search_ts.staswith("PB"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="PB [text]",
                    description="Search For Torrent in ThePirateBay ...",
                    input_message_content=InputTextMessageContent(
                        message_text="`PB [text]`\n\nSearch ThePirateBay Torrents from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔍Search Again", switch_inline_query_current_chat="PB ")]])
                )
            )
        else:
            results = play_scraper.search(update.query)
            if not results:
                answers.append(
                InlineQueryResultArticle(
                    title=result["title"],
                    description=result.get("description", None),
                    thumb_url=result.get("icon", None),
                    input_message_content=InputTextMessageContent(
                        message_text=details, disable_web_page_preview=True
                    ),
                    reply_markup=reply_markup
                )
            )
        
            else:
                for i in range(len(torrentList)):
                    answers.append(
                        InlineQueryResultArticle(
                            title=f"{torrentList[i]['Name']}",
                            description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}",
                            input_message_content=InputTextMessageContent(
                                message_text=f"**Title:** `{}`".format(result["title"]) + "\n" \
                                             f"**Description:** `{}`".format(result["description"]) + "\n" \
                                             f"**App ID:** `{}`".format(result["app_id"]) + "\n" \
                                             f"**Developer:** `{}`".format(result["developer"]) + "\n" \
                                             f"**Developer ID:** `{}`".format(result["developer_id"]) + "\n" \
                                             f"**Score:** `{}`".format(result["score"]) + "\n" \
                                             f"**Price:** `{}`".format(result["price"]) + "\n" \
                                             f"**Full Price:** `{}`".format(result["full_price"]) + "\n" \
                                             f"**Free:** `{}`".format(result["free"]) + "\n" \
                                             f"\n" + "Made by @FayasNoushad",
                                parse_mode="Markdown"
                            ),
                            reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton("𝗦𝗲𝗮𝗿𝗰𝗵 𝗔𝗴𝗮𝗶𝗻 🌶✨", switch_inline_query_current_chat="PB ")]])
                        )
                    )

except Exception as error:
            print(error)
    await update.answer(answers)



      try:
        await inline.answer(
            results=answers,
            cache_time=0
        )
        print(f"[{Config.SESSION_NAME}] - Answered Successfully - {inline.from_user.first_name}")
    except QueryIdInvalid:
        print(f"[{Config.SESSION_NAME}] - Failed to Answer - {inline.from_user.first_name} - Sleeping for 5s")
        await asyncio.sleep(5)
        try:
            await inline.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out!",
                switch_pm_parameter="sta",
            )
        except QueryIdInvalid:
            print(f"[{Config.SESSION_NAME}] - Failed to Answer Error - {inline.from_user.first_name} - Sleeping for 5s")
            await asyncio.sleep(5)


