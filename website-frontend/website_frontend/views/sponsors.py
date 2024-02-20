import reflex as rx
import website_frontend.constants as const

from website_frontend.styles.styles import Size
from website_frontend.components.title import title
from website_frontend.components.link_sponsor import link_sponsor

def sponsors() -> rx.Component:
    return rx.chakra.vstack(
        title("Colaboran"),
        rx.chakra.responsive_grid(
            link_sponsor(
                "/elgato.png",
                const.ELGATO_URL,
                "Logotipo de Elgato"
            ),
            link_sponsor(
                "/mvp.png",
                const.MVP_URL,
                "Logotipo de Microsoft MVP"
            ),
            link_sponsor(
                "/githubstar.png",
                const.GITHUB_STAR_URL,
                "Logotipo de GitHub Star"
            ),
            spacing=Size.BIG.value,
            columns=[1, 3]
        ),
        width="100%",
        align_items="start",
        spacing=Size.MEDIUM.value
    )