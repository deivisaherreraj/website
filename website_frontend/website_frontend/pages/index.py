import reflex as rx
import website_frontend.utils as utils
import website_frontend.styles.styles as styles

from website_frontend.views.navbar import navbar
from website_frontend.views.header import header
from website_frontend.views.links import links
from website_frontend.views.sponsors import sponsors
from website_frontend.views.footer import footer
from website_frontend.styles.styles import Size
from website_frontend.state.PageState import PageState

@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
    on_load=PageState.check_live
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(
                    live=PageState.live_status,
                    live_title=PageState.live_title
                ),
                links(),
                # TODO Habilitar función solo cuando se tenga lo necesario
                # sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )