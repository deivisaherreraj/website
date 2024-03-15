import reflex as rx
import datetime
import website_frontend.constants as const

from website_frontend.styles.styles import Size, Spacing
from website_frontend.styles.colors import Color, TextColor
from website_frontend.components.link_icon import link_icon
from website_frontend.components.info_text import info_text

def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
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
                        "/icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"
                    ),
                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
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
                    rx.spacer(),
                    info_text(
                        "0+", 
                        "aplicaciones creadas"
                    ),
                    width="100%"
                ),
                rx.text(
                    f"""
                    Soy ingeniero de software, un apasionado del desarrollo de software y la tecnología.
                    Actualmente trabajo como full-stack developer, mi enfoque se basa en la integración de las tecnologías 
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