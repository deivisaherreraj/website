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
            "Guías y tutoriales",
            "Consulta mis tutoriales para aprender programación",
            "/icons/code.svg",
            Route.COURSES.value,
            True,
            False,
            Color.SECONDARY.value
        ),
        link_button(
            "Discord",
            "El chat y los grupos de estudio de la comunidad",
            "/icons/discord.svg",
            const.DISCORD_URL
        ),
        
        title("Plataformas de trabajo"),
        link_button(
            "Workana",
            "Perfil de Workana donde ofrezco mis servicios como freelance",
            "/icons/freelancer.svg",
            const.WORKANA_URL
        ),
        link_button(
            "Gumroad",
            "Mi tienda en Gumroad donde vendo recursos, cursos, o productos digitales",
            "/icons/gumroad.svg",
            const.GUMROAD_URL
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