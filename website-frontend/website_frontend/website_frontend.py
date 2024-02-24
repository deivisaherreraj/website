import reflex as rx
import website_frontend.constants as const
import website_frontend.styles.styles as styles

from website_frontend.pages.index import index
from website_frontend.pages.courses import courses

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
