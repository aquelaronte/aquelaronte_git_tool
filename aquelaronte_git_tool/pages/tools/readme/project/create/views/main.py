import reflex as rx
from ..state import ProjectState
from . import description, guides, header, type, download


def main() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    "Project README",
                    size="9",
                    weight="bold",
                    style=rx.style.Style({"color": "var(--accent-9)"}),
                ),
                rx.text("Customize your project README."),
                align="center",
                width="100vw",
            ),
            align="start",
            justify="start",
            width="100vw",
        ),
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Type", value="1"),
                rx.tabs.trigger("Header", value="2"),
                rx.tabs.trigger("Description", value="3"),
                rx.tabs.trigger("Guides", value="4"),
                rx.tabs.trigger("Download", value="5"),
            ),
            rx.tabs.content(
                rx.box(
                    type.type(),
                    style=rx.style.Style(
                        {"height": "auto", "min-height": "80vh", "width": "100vw"}
                    ),
                ),
                value="1",
            ),
            rx.tabs.content(
                rx.box(
                    header.header(),
                    style=rx.style.Style(
                        {"height": "auto", "min-height": "80vh", "width": "100vw"}
                    ),
                ),
                value="2",
            ),
            rx.tabs.content(
                rx.box(
                    description.description(),
                    style=rx.style.Style(
                        {"height": "auto", "min-height": "80vh", "width": "100vw"}
                    ),
                ),
                value="3",
            ),
            rx.tabs.content(
                rx.box(
                    guides.guides(),
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
                        {"height": "auto", "min-height": "80vh", "width": "100vw"}
                    ),
                ),
                value="5",
            ),
            on_change=lambda e: ProjectState.set_tab_value(e),
            value=ProjectState.tab_value,
        ),
    )
