import reflex as rx
import website_frontend.utils as utils
import website_frontend.constants as const

from website_frontend.api.api import live

class PageState(rx.State):
    live_status: bool
    
    async def check_live(self):
        self.live_status = await live(const.USER)