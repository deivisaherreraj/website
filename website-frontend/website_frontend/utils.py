import reflex as rx

# Común
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "https://dherrerajdev.netlify.app/preview.png"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@dherrerajdev"}
]

# Index
index_title = "DHerreraJDev | Desarrollo de software Full-Stack"
index_description = "Hola, mi nombre es Deivis Andres Herrera Julio. Soy ingeniero de software, desarrollador Full-Stack."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# Cursos

courses_title = "DHerreraJDev | Cursos gratis de programación"
courses_description = "Este es un listado con algunos cursos gratis para aprender programación y desarrollo de software."

courses_meta = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description},
]
courses_meta.extend(_meta)