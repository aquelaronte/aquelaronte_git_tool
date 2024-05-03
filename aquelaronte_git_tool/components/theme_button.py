import reflex as rx
from aquelaronte_git_tool.pages.global_state import GlobalState


def theme_button(color_name: str, color: str, navbar_color: str) -> rx.Component:
    return (
        rx.box(
            style=rx.style.Style(
                {
                    "height": "30px",
                    "width": "30px",
                    "border-radius": "10px",
                    "background-color": color,
                    "cursor": "pointer",
                }
            ),
            on_click=GlobalState.change_accent(color_name, navbar_color),
        ),
    )
