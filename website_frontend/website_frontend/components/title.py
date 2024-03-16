import reflex as rx
import website_frontend.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style=styles.title_style
    )