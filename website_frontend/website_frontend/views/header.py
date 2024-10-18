import reflex as rx
import datetime
import website_frontend.constants as const

from website_frontend.styles.styles import Size, Spacing
from website_frontend.styles.colors import Color, TextColor
from website_frontend.components.link_icon import link_icon
from website_frontend.components.info_text import info_text
from website_frontend.components.link_button import link_button

def header(details=True, live=False, live_title="") -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.cond(
                    live,
                    rx.link(
                        rx.image(
                            src="/icons/twitch.svg",
                            height=Size.DEFAULT.value,
                            width=Size.DEFAULT.value
                        ),
                        href=const.TWITCH_URL,
                        is_external=True,
                        class_name="blink",
                        border_radius="50%",
                        padding=Size.SMALL.value,
                        bg=Color.PURPLE.value,
                        position="absolute",
                        bottom="0",
                        right="0"
                    )
                ),
                rx.avatar(
                    name="Deivis Herrera",
                    size=Spacing.MEDIUM_BIG.value,
                    src="/avatar.jpeg",
                    radius="full",
                    color=TextColor.BODY.value,
                    bg=Color.CONTENT.value,
                    padding="2px",
                    border=f"4px solid {Color.PRIMARY.value}"
                ),
                position="relative"
            ),
            rx.vstack(
                rx.heading(
                    "Deivis Herrera Julio",
                    size=Spacing.BIG.value
                ),
                rx.text(
                    "@dherrerajdev",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "/icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    spacing=Spacing.LARGE.value,
                    padding_top=Size.SMALL.value
                ),
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing=Spacing.DEFAULT.value
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text(
                        f"{experience()}+",
                        "años de experiencia"
                    ),
                    width="100%"
                ),
                rx.cond(
                    live,
                    link_button(
                        "En directo",
                        live_title,
                        "/icons/twitch.svg",
                        const.TWITCH_URL,
                        False,
                        True,
                        Color.PURPLE.value
                    )
                ),
                rx.text(
                    f"""
                    Soy full-stack developer, un apasionado del desarrollo de software y la tecnología, 
                    mi enfoque se basa en la integración de las tecnologías 
                    más avanzadas en el ámbito del Back-End y Front-End y así explorar nuevas ideas y trabajar en proyectos emocionantes. 
                    Aquí podrás encontrar todos mis enlaces de interés !Bienvenido/a¡
                    """,
                    font_size=Size.DEFAULT.value,
                    color=TextColor.BODY.value
                ),
                width="100%",
                spacing=Spacing.BIG.value
            )
        ),
        width="100%",
        spacing=Spacing.BIG.value,
        align_items="start"
    )


def experience() -> int:
    return datetime.date.today().year - 2013