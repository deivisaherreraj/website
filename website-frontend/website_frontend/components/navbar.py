import reflex as rx
import website_frontend.styles.styles as styles

from website_frontend.routes import Route
from website_frontend.styles.styles import Size
from website_frontend.styles.colors import Color


def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.link(
            rx.box(
                rx.chakra.span("dherreraj", color=Color.PRIMARY.value),
                rx.chakra.span("dev", color=Color.SECONDARY.value),
                style=styles.navbar_title_style
            ),
            href=Route.INDEX.value
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )