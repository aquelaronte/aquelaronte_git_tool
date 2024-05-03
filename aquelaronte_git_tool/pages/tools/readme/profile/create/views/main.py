import reflex as rx
from . import tastes, tech_stack, stats, contact, download
from ..state import State


def main() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    "Profile README",
                    size="9",
                    weight="bold",
                    style=rx.style.Style({"color": "var(--accent-9)"}),
                ),
                rx.text("Customize your profile README."),
                align="center",
                width="100vw",
            ),
            align="start",
            justify="start",
            width="100vw",
        ),
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Tastes", value="1"),
                rx.tabs.trigger("Tech Stack", value="2"),
                rx.tabs.trigger("Stats", value="3"),
                rx.tabs.trigger("Contact", value="4"),
                rx.tabs.trigger("Download", value="5"),
            ),
            rx.tabs.content(
                rx.box(
                    tastes.tastes(),
                    style=rx.style.Style(
                        {"height": "auto", "min-height": "80vh", "width": "100vw"}
                    ),
                ),
                value="1",
            ),
            rx.tabs.content(
                rx.box(
                    tech_stack.tech_stack(),
                    style=rx.style.Style(
                        {"height": "auto", "min-height": "80vh", "width": "100vw"}
                    ),
                ),
                value="2",
            ),
            rx.tabs.content(
                rx.box(
                    stats.stats(),
                    style=rx.style.Style(
                        {"height": "auto", "min-height": "80vh", "width": "100vw"}
                    ),
                ),
                value="3",
            ),
            rx.tabs.content(
                rx.box(
                    contact.contact(),
                    style=rx.style.Style(
                        {"height": "auto", "min-height": "80vh", "width": "100vw"}
                    ),
                ),
                value="4",
            ),
            rx.tabs.content(
                rx.box(
                    download.download(),
                    style=rx.style.Style(
                        {"height": "auto", "min-height": "100vh", "width": "100vw"}
                    ),
                ),
                value="5",
            ),
            on_change=lambda value: State.set_tab_value(value),
            value=State.tab_value,
        ),
    )
