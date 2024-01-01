from pyrogram.types import InlineKeyboardButton

import config
from InflexMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝐀ԃ𝐃 𝐌ҽ 𝐓σ 𝐘συ𝐑 𝐆ɾσυ𝐏"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["𝐆ɾσυ𝐏"], url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝐀ԃ𝐃 𝐌ҽ 𝐓σ 𝐘συ𝐑 𝐆ɾσυ𝐏"],
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ],
        [InlineKeyboardButton(text=_["𝐂σɱɱαɳԃ𝐒"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["𝐔ρ∂αтє𝐒"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["𝐆ɾσυ𝐏"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["𝐅συɳԃҽ𝐑"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_7"], url=config.UPSTREAM_REPO),
        ],
    ]
    return buttons
