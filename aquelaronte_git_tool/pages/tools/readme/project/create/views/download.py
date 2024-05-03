import reflex as rx
from ..state import ProjectState


def download() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading(
                "Download",
                size="6",
                weight="bold",
                style=rx.style.Style({"color": "var(--accent-9)"}),
            ),
            rx.box(height="10px"),
            rx.hstack(
                rx.button(
                    "Download",
                    on_click=ProjectState.download_file,
                    style=rx.style.Style({"cursor": "pointer"}),
                ),
                rx.popover.root(
                    rx.popover.trigger(
                        rx.button(
                            "Copy to clipboard",
                            on_click=rx.set_clipboard(ProjectState.preview_markdown),
                            style=rx.style.Style({"cursor": "pointer"}),
                        ),
                    ),
                    rx.popover.content(
                        rx.flex(
                            rx.text("README.md copied to clipboard"),
                            rx.popover.close(
                                rx.button(
                                    "ok", style=rx.style.Style({"cursor": "pointer"})
                                )
                            ),
                            direction="column",
                            spacing="3",
                        )
                    ),
                ),
            ),
            rx.box(height="25px"),
            rx.heading(
                "Preview",
                size="5",
                weight="bold",
            ),
            rx.box(height="10px"),
            rx.card(rx.markdown(ProjectState.preview_markdown)),
            align="center",
            padding_y="26px",
            width="100vw",
        )
    )
