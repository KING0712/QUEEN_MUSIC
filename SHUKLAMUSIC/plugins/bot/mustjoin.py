
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from SHUKLAMUSIC import app

#--------------------------

MUST_JOIN = "KING_BHAI_BABY"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/5a37d74a59f00043d64f9.jpg", caption=f"𝐎ʏʏ 𝐏ᴀʜᴀʟᴇ [🖤 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🖤]({link}) 𝐆ʀᴏᴜᴘ 𝐉ᴏɪɴ 𝐊ᴀʀ... 𝐀ᴜʀ [🖤 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🖤]({link}) 𝐉ᴏɪɴ 𝐊ᴀʀɴᴇ 𝐊ᴇ 𝐁ᴀᴀᴅ 𝐇ɪ 𝐁ᴏᴛ 𝐒ᴛᴀʀᴛ 𝐇ᴏɢᴀ 😈 ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("😈 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏 😈", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_Jᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")
