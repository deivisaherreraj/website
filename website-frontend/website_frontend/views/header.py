import reflex as rx
import datetime
import website_frontend.constants as const

from website_frontend.styles.styles import Size
from website_frontend.styles.colors import Color, TextColor
from website_frontend.components.link_icon import link_icon
from website_frontend.components.info_text import info_text


def header() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
            rx.chakra.avatar(                
                name="Deivis Herrera",
                size="xl",
                src="/avatar.jpeg",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.chakra.vstack(
                rx.heading(
                    "Deivis Herrera Julio",
                    size="7"
                ),
                rx.text(
                    "@dherrerajdev",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.chakra.hstack(
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
                    spacing=Size.LARGE.value
                ),
                align_items="start"
            ),
            spacing=Size.DEFAULT.value
        ),
        rx.chakra.vstack(
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
                rx.spacer(),
                info_text(
                    "0+", 
                    "seguidores"
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
            spacing=Size.BIG.value
        ),
        width="100%",
        spacing=Size.BIG.value,
        align_items="start"
    )


def experience() -> int:
    return datetime.date.today().year - 2013