import reflex as rx

from website_frontend.styles.styles import Size
from website_frontend.styles.colors import Color, TextColor


def info_text(title: str, subTitle: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            as_="span",
            font_weight="bold",
            color=Color.PRIMARY.value
        ),
        f" {subTitle}",
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value
    )