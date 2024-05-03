import reflex as rx
from ..state import State


def stats() -> rx.Component:
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
                rx.input.input(
                    placeholder="Enter your github username then press enter",
                    tab_index=1,
                    on_change=State.set_username,
                    on_key_down=State.handle_enter,
                ),
                size="3",
                style=rx.style.Style(
                    {"width": "60%"},
                ),
            ),
            rx.box(height="30px"),
            rx.cond(
                State.stats_have_data,
                rx.vstack(
                    rx.foreach(State.stats, lambda x: rx.image(src=x)),
                    justify="center",
                    align="center",
                ),
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
                    on_click=lambda: State.set_tab_value("2"),
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
                    on_click=lambda: State.submit_stats(),
                    tab_index=5,
                ),
                width="100vw",
                align="center",
                justify="center",
            ),
            align="center",
            width="100vw",
            padding_y="26px",
        )
    )
