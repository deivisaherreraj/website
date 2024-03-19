import reflex as rx

class Live(rx.Base):
    live: bool
    title: str
    category: str    
    tags: list[str]
    viewer: int