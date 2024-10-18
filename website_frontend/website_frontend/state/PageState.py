import reflex as rx
import website_frontend.utils as utils
import website_frontend.constants as const

from website_frontend.model.Live import Live
from website_frontend.api.api import live

class PageState(rx.State):
    live_status: bool
    live_title: str
    
    async def check_live(self):
        live_object = await live(const.USER)
        self.live_status = live_object["live"]
        self.live_title = live_object["title"]