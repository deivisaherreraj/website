import reflex as rx
import datetime
import website_frontend.constants as const

from website_frontend.styles.styles import Size
from website_frontend.styles.colors import Color, TextColor

def footer() -> rx.Component:
    return rx.chakra.vstack(
        rx.image(
            src="/logo.png",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotipo de DHerreraJDev. Una doble > &quot;de&quot; _."
        ),
        rx.link(
            rx.box(
                f"Copyright © 2023-{datetime.date.today().year} ",
                rx.chakra.span("DHerreraJDev by Deivis Andres Herrera Julio", color=Color.PRIMARY.value),
                " v1.",
                padding_top=Size.DEFAULT.value,
                color=TextColor.BODY.value
            ),
            href=const.DHERRERAJDEV_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.chakra.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value
                ),
                rx.text(
                    "CONSTRUYENDO SOFTWARE CON ♥ DESDE COLOMBIA PARA EL MUNDO.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
            ),
            href=const.REPO_URL,
            is_external=True
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.ZERO.value,
        color=TextColor.FOOTER.value
    )