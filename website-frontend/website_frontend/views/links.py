import reflex as rx
import website_frontend.constants as const

from website_frontend.routes import Route
from website_frontend.components.link_button import link_button
from website_frontend.components.title import title
from website_frontend.styles.styles import Size, Color


def links() -> rx.Component:
    return rx.chakra.vstack(
        title("Comunidad"),
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
            const.SETUP_URL,
            False
        ),
        link_button(
            "DherrerajDev",
            "Mi sitio web",
            "/icons/developer.svg",
            const.DHERRERAJDEV_URL,
            True,
            Color.SECONDARY.value
        ),
        link_button(
            "Invítame a un café",
            "¿Quieres ayudarme a que siga creando contenido?",
            "/icons/coffee.svg",
            const.COFFEE_URL,
            False
        ),

        title("Contacto"),
        link_button(
            "MyPublicInbox",
            "Respuesta rápida y con preferencia",
            "/icons/checkemail.svg",
            Route.INDEX.value,
            False
        ),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        width="100%",
        spacing=Size.DEFAULT.value,
    )