import reflex as rx
from aquelaronte_git_tool.pages.tools.readme.profile.create.state import (
    State,
)


def stack_button(language: dict) -> rx.Component:

    return rx.fragment(
        rx.cond(
            language["selected"] == True,
            rx.button(
                rx.hstack(
                    rx.text(language["name"], size="3", weight="bold"),
                    rx.icon("x", size=20),
                    justify="between",
                    align="center",
                    height="100%",
                ),
                size="3",
                variant="solid",
                on_click=lambda: State.remove_tech_stack(language),
                style=rx.style.Style({"cursor": "pointer", "transition": "all 0.3s"}),
            ),
            rx.button(
                rx.hstack(
                    rx.text(language["name"], size="3", weight="bold"),
                    rx.icon("plus", size=20),
                    justify="center",
                    align="center",
                ),
                size="3",
                variant="soft",
                on_click=lambda: State.append_tech_stack(language),
                style=rx.style.Style({"cursor": "pointer", "transition": "all 0.3s"}),
            ),
        ),
    )
