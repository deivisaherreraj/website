import reflex as rx
import website_frontend.constants as const

from website_frontend.routes import Route
from website_frontend.components.link_button import link_button
from website_frontend.components.title import title
from website_frontend.styles.styles import Color, Spacing


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Guías y tutoriales gratis",
            "Consulta mis tutoriales para aprender programación",
            "/icons/code.svg",
            Route.COURSES.value,
            False,
            False,
            Color.SECONDARY.value
        ),
        link_button(
            "Twitch",
            "Transmisiones sobre programación de lunes a viernes",
            "/icons/twitch.svg",
            const.TWITCH_URL
        ),
        link_button(
            "Discord",
            "El chat y los grupos de estudio de la comunidad",
            "/icons/discord.svg",
            const.DISCORD_URL
        ),
        link_button(
            "YouTube",
            "Tutoriales sobre desarrollo de software semanales",
            "/icons/youtube.svg",
            const.YOUTUBE_URL
        ),
                
        title("Recursos y más"),        
        link_button(
            "Mi setup",
            "Listado con todos los elementos que uso en mi trabajo",
            "/icons/setup.svg",
            Route.INDEX.value,
            True,
            False
        ),
        link_button(
            "DHerreraJDev",
            "Mi sitio web",
            "/icons/developer.svg",
            const.DHERRERAJDEV_URL,
            False,
            True,            
            Color.SECONDARY.value
        ),
        link_button(
            "Invítame a un café",
            "¿Quieres ayudarme a que siga creando contenido?",
            "/icons/coffee.svg",
            const.COFFEE_URL,
            False,
            False
        ),

        title("Contacto"),
        link_button(
            "My Public Inbox",
            "Respuesta rápida y con preferencia",
            "/icons/checkemail.svg",
            Route.INDEX.value,
            True,
            False
        ),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )