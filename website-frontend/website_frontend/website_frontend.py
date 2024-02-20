"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
import website_frontend.constants as const
import website_frontend.styles.styles as styles

# class State(rx.State):
#     pass

def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),            
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title = "DherrerajDev | Te enseño programación y desarrollo de software",
    description = "Hola, mi nombre es Deivis Herrera Julio. Soy ingeniero de software, desarrollador full-stack."
)
