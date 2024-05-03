import reflex as rx
from ..state import State
from aquelaronte_git_tool.components import stack_button


def tech_stack() -> rx.Component:

    return rx.fragment(
        rx.vstack(
            rx.heading(
                "Tech stack",
                size="6",
                weight="bold",
                style=rx.style.Style({"color": "var(--accent-9)"}),
            ),
            rx.box(height="25px"),
            rx.heading(
                "Selected",
                size="5",
                weight="bold",
            ),
            rx.grid(
                rx.foreach(
                    State.tech_stack_selected,
                    stack_button.stack_button,
                ),
                columns="11",
                spacing="1",
            ),
            rx.box(height="10px"),
            rx.heading(
                "Languages",
                size="5",
                weight="bold",
            ),
            rx.box(height="10px"),
            rx.grid(
                rx.foreach(
                    State.tech_stack_languages,
                    stack_button.stack_button,
                ),
                columns="11",
                spacing="1",
            ),
            rx.box(height="20px"),
            rx.heading(
                "Frameworks",
                size="5",
                weight="bold",
            ),
            rx.box(height="10px"),
            rx.grid(
                rx.foreach(
                    State.tech_stack_frameworks,
                    stack_button.stack_button,
                ),
                columns="11",
                spacing="1",
            ),
            rx.box(height="10px"),
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
                    on_click=lambda: State.set_tab_value("1"),
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
                    on_click=lambda: State.submit_tech_stack(),
                    tab_index=5,
                ),
                width="100vw",
                align="center",
                justify="center",
            ),
            align="center",
            padding_y="26px",
            width="100vw",
        )
    )
