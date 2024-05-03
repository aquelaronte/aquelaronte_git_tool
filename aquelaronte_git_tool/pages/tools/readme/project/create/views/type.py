import reflex as rx
from aquelaronte_git_tool.components import presentation_card
from ..state import ProjectState


def type() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading(
                "Select your project type",
                size="6",
                weight="bold",
                style=rx.style.Style({"color": "var(--accent-9)"}),
            ),
            rx.box(height="25px"),
            rx.grid(
                rx.container(
                    presentation_card.presentation_card(
                        "server", "API", "customize your API readme"
                    ),
                    on_click=lambda: ProjectState.set_project_type("api"),
                    style=rx.style.Style({"cursor": "pointer"}),
                ),
                rx.container(
                    presentation_card.presentation_card(
                        "panels-top-left", "Web page", "customize your Web page readme"
                    ),
                    on_click=lambda: ProjectState.set_project_type("web"),
                    style=rx.style.Style({"cursor": "pointer"}),
                ),
                spacing="4",
            ),
            align="center",
            padding_y="26px",
            width="100vw",
        )
    )
