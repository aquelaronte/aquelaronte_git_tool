import reflex as rx
from aquelaronte_git_tool.components import navbar
from .views import main


def page() -> rx.Component:
    return rx.vstack(
        navbar.navbar(),
        main.main(),
        justify="center",
        align="center",
    )
