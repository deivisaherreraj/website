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

# Google tag (gtag.js)
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"
        ),
        rx.script(
            f"""
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{const.G_TAG}');
            """
        ),
    ],
)

title = "DHerreraJDev | Desarrollo de software Full-Stack"
description = "Hola, mi nombre es Deivis Andres Herrera Julio. Soy ingeniero de software, desarrollador Full-Stack."
preview = "https://dherrerajdev.netlify.app/preview.png"
    
app.add_page(
    index,
    title = title,
    description = description,
    image = preview,
    meta = [
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@dherrerajdev"}
    ]
)
