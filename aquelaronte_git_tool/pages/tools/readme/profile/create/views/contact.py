import reflex as rx
from ..state import State


def contact() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading(
                "Tech stack",
                size="6",
                weight="bold",
                style=rx.style.Style({"color": "var(--accent-9)"}),
            ),
            rx.box(height="25px"),
            rx.input.root(
                rx.input.slot(rx.icon("phone")),
                rx.input.input(
                    placeholder="Input your contact number (with country code)",
                    tab_index=1,
                    on_change=State.set_first_contact,
                ),
                size="3",
                style=rx.style.Style(
                    {"width": "60%"},
                ),
            ),
            rx.box(height="10px"),
            rx.input.root(
                rx.input.slot(rx.icon("hash")),
                rx.input.input(
                    placeholder="Input your instagram link",
                    tab_index=1,
                    on_change=State.set_second_contact,
                ),
                size="3",
                style=rx.style.Style(
                    {"width": "60%"},
                ),
            ),
            rx.box(height="10px"),
            rx.input.root(
                rx.input.slot(rx.icon("linkedin")),
                rx.input.input(
                    placeholder="Input your linkedin link",
                    tab_index=1,
                    on_change=State.set_third_contact,
                ),
                size="3",
                style=rx.style.Style(
                    {"width": "60%"},
                ),
            ),
            rx.box(height="10px"),
            rx.input.root(
                rx.input.slot(rx.icon("codepen")),
                rx.input.input(
                    placeholder="Input your codepen link",
                    tab_index=1,
                    on_change=State.set_fourth_contact,
                ),
                size="3",
                style=rx.style.Style(
                    {"width": "60%"},
                ),
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
                    on_click=lambda: State.set_tab_value("3"),
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
                    on_click=lambda: State.submit_contacts,
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
