import reflex as rx
from ..state import State


def tastes() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading(
                "Tastes",
                size="6",
                weight="bold",
                style=rx.style.Style({"color": "var(--accent-9)"}),
            ),
            rx.box(height="25px"),
            rx.input.root(
                rx.input.slot(rx.text("🔭")),
                rx.input.input(
                    placeholder="What are you looking for?",
                    tab_index=1,
                    on_blur=State.set_first_taste,
                ),
                size="3",
                style=rx.style.Style(
                    {"width": "70%"},
                ),
            ),
            rx.input.root(
                rx.input.slot(rx.text("🌱")),
                rx.input.input(
                    placeholder="Are you working on something?",
                    tab_index=2,
                    on_blur=State.set_second_taste,
                ),
                size="3",
                style=rx.style.Style({"width": "70%"}),
            ),
            rx.input.root(
                rx.input.slot(rx.text("💬")),
                rx.input.input(
                    placeholder="Are you learning something?",
                    tab_index=3,
                    on_blur=State.set_third_taste,
                ),
                size="3",
                style=rx.style.Style({"width": "70%"}),
            ),
            rx.input.root(
                rx.input.slot(rx.text("👯")),
                rx.input.input(
                    placeholder="Your favorite programming language?",
                    tab_index=4,
                    on_blur=State.set_fourth_taste,
                ),
                size="3",
                style=rx.style.Style({"width": "70%"}),
            ),
            rx.box(height="10px"),
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
                on_click=State.submit_tastes,
                tab_index=5,
            ),
            align="center",
            padding_y="26px",
            width="100vw",
        ),
    )
