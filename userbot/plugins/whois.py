"""Get Telegram Profile Picture and other information
Syntax: .whois @username"""

import html
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from userbot.utils import admin_cmd


@borg.on_cmd("whois", about="""\
__use this to get any user details__

**Usage:**
`just reply to any user message or add user_id or username`
**Example:**

    `.whois [user_id | username]`""")
async def who_is(message: Message):
    await message.edit("`Collecting Whois Info.. Hang on!`")
    user_id = message.input_str

    if user_id:
        try:
            from_user = await userge.get_users(user_id)
            from_chat = await userge.get_chat(user_id)

        except:
            await message.err(
                text="`no valid user_id or message specified, do .help whois for more info`")
            return

    elif message.reply_to_message:
        from_user = await userge.get_users(message.reply_to_message.from_user.id)
        from_chat = await userge.get_chat(message.reply_to_message.from_user.id)

    else:
        await message.err(
            text="`no valid user_id or message specified, do .help whois for more info`")
        return

    if from_user or from_chat is not None:
        message_out_str = ""

        message_out_str += f"<b>USER INFO:</b>\n\n"
        message_out_str += f"<b>🗣 First Name:</b> <code>{from_user.first_name}</code>\n"
        message_out_str += f"<b>🗣 Last Name:</b> <code>{from_user.last_name}</code>\n"
        message_out_str += f"<b>👤 Username:</b> @{from_user.username}\n"
        message_out_str += f"<b>🏢 DC ID:</b> <code>{from_user.dc_id}</code>\n"
        message_out_str += f"<b>🤖 Is Bot:</b> <code>{from_user.is_bot}</code>\n"
        message_out_str += f"<b>🚫 Is Restricted:</b> <code>{from_user.is_scam}</code>\n"
        message_out_str += f"<b>✅ Is Verified by Telegram:</b> <code>{from_user.is_verified}</code>\n"
        message_out_str += f"<b>🕵️‍♂️ User ID:</b> <code>{from_user.id}</code>\n"
        message_out_str += f"<b>📞 Phone NO:</b> <code>{from_user.phone_number}</code>\n\n"
        message_out_str += f"<b>📝 Bio:</b> <code>{from_chat.description}</code>\n\n"
        message_out_str += f"<b>👁 Last Seen:</b> <code>{from_user.status}</code>\n"
        message_out_str += f"<b>🔗 Permanent Link To Profile:</b> <a href='tg://user?id={from_user.id}'>{from_user.first_name}</a>"

        if from_user.photo:
            local_user_photo = await userge.download_media(message=from_user.photo.big_file_id)

            await userge.send_photo(chat_id=message.chat.id,
                                    photo=local_user_photo,
                                    caption=message_out_str,
                                    parse_mode="html",
                                    disable_notification=True)

            os.remove(local_user_photo)
            await message.delete()

        else:
            message_out_str = "<b>📷 NO DP Found 📷</b>\n
