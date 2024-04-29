import math
from config import SUPPORT_CHAT, OWNER_USERNAME
from pyrogram.types import InlineKeyboardButton
from SHUKLAMUSIC import app
import config
from SHUKLAMUSIC.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـ😘ﮩ꯭ﮩـ"
    elif 10 < umm < 20:
        bar = "ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـ🥀ﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩـ"
    elif 20 <= umm < 30:
        bar = "ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ🍃ـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩـ"
    elif 30 <= umm < 40:
        bar = "ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩ٨꯭ـﮩ😂ـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩـ"
    elif 40 <= umm < 50:
        bar = "ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭😍ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩـ"
    elif 50 <= umm < 60:
        bar = "ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩ🙃ـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩـ"
    elif 60 <= umm < 70:
        bar = "ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭😜ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩـ"
    elif 70 <= umm < 80:
        bar = "ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـ😇ﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩـ"
    elif 80 <= umm < 95:
        bar = "ـﮩ꯭😈ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩـ"
    else:
        bar = "ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭꯭ﮩ٨꯭ـﮩـ꯭꯭꯭꯭٨꯭ـﮩ꯭ﮩـ"
    buttons = [
                [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="🇰", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="🇮", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="🇳", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="🇬", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
         InlineKeyboardButton(text="😈 𝐎𝐖𝐍𝐄𝐑 😈", user_id=config.OWNER_ID),
         InlineKeyboardButton(text="🥺 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🥺", url=f"{SUPPORT_CHAT}",),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="🇰", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="🇮", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="🇳", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="🇬", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
         InlineKeyboardButton(text="😈 𝐎𝐖𝐍𝐄𝐑 😈", user_id=config.OWNER_ID),
         InlineKeyboardButton(text="🥺 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🥺", url=f"{SUPPORT_CHAT}",),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"SHUKLAPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"SHUKLAPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
