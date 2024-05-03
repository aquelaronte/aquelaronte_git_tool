import reflex as rx
from ..state import ProjectState


def description() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading(
                "Input your description for your project",
                size="6",
                weight="bold",
                style=rx.style.Style({"color": "var(--accent-9)"}),
            ),
            rx.box(height="25px"),
            rx.heading(f"Subtitle for project", size="3"),
            rx.text_area(
                placeholder="What type of content will be in this repositorio example: 'This repository contains AGTool source code'",
                style=rx.style.Style({"width": "50%", "height": "100px"}),
                on_change=ProjectState.set_first_description,
            ),
            rx.box(height="10px"),
            rx.heading(f"Why {ProjectState.project_name}?", size="3"),
            rx.text_area(
                placeholder="Explain why this project is important, what it does, and what it can be used for",
                style=rx.style.Style({"width": "50%", "height": "100px"}),
                on_change=ProjectState.set_second_description,
            ),
            rx.hstack(
                rx.button(
                    rx.hstack(
                        rx.icon(
                            "arrow-left",
                            style=rx.style.Style({"color": "var(--accent-9)"}),
                        ),
                        rx.text("Back"),
                    ),
                    style=rx.style.Style({"cursor": "pointer"}),
                    variant="outline",
                    on_click=lambda: ProjectState.set_tab_value("2"),
                    tab_index=5,
                ),
                rx.button(
                    rx.hstack(
                        rx.text("Next"),
                        rx.icon(
                            "arrow-right",
                            style=rx.style.Style({"color": "var(--accent-9)"}),
                        ),
                    ),
                    style=rx.style.Style({"cursor": "pointer"}),
                    variant="outline",
                    on_click=lambda: ProjectState.submit_description(),
                    tab_index=5,
                ),
            ),
            align="center",
            padding_y="26px",
            width="100vw",
        )
    )
