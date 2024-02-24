import reflex as rx
import website_frontend.styles.styles as styles

from website_frontend.styles.styles import Size, Color, Spacing


def link_button(title: str, subTitle: str, image: str, url: str, is_disabled=False, is_external=True, highlight_color=None) -> rx.Component:
    return rx.link(
        rx.chakra.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(
                        title,
                        size=Spacing.SMALL.value,
                        style=styles.button_title_style
                    ),
                    rx.text(
                        subTitle,
                        size=Spacing.VERY_SMALL.value,
                        style=styles.button_body_style
                    ),
                    align_items="start",
                    spacing=Spacing.VERY_SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                align="center",
                width="100%"
            ),
            is_disabled=is_disabled,
            border_color=highlight_color,
            border_width="2px" if highlight_color != None else None            
        ),
        href=url,
        is_external=is_external,
        width="100%"
    )