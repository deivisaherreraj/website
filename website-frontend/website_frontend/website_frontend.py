"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
import website_frontend.constants as const
import website_frontend.styles.styles as styles

from website_frontend.components.navbar import navbar
from website_frontend.views.header import header
from website_frontend.views.links import links
from website_frontend.views.sponsors import sponsors
from website_frontend.components.footer import footer
from website_frontend.styles.styles import Size

# class State(rx.State):
#     pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.chakra.vstack(
                header(),
                links(),
                # sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title = "DherrerajDev | Te enseño programación y desarrollo de software",
    description = "Hola, mi nombre es Deivis Herrera Julio. Soy ingeniero de software, desarrollador full-stack."
)
