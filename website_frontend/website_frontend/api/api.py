import website_frontend.constants as const

from website_frontend.model.Live import Live
from .TwitchAPI import TwitchAPI

TWITCH_API = TwitchAPI()

async def repo() -> str:
    return const.REPO_URL

async def live(user: str) -> dict:    
    return TWITCH_API.live(user)