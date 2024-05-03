import reflex as rx
from aquelaronte_git_tool.pages.global_state import GlobalState
from aquelaronte_git_tool.components import theme_button


def navbar() -> rx.Component:
    return rx.fragment(
        rx.hstack(
            rx.box(
                rx.hstack(
                    rx.text(
                        "AGTool",
                        weight="bold",
                        style=rx.style.Style(
                            {
                                "color": "var(--accent-9)",
                                "font-size": "2.5rem",
                                "letter-spacing": "0.2rem",
                            }
                        ),
                    ),
                    rx.icon("github", size=35, stroke_width=2),
                    align="center",
                    justify="center",
                ),
            ),
            rx.box(
                rx.hstack(
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("home"),
                                rx.text(
                                    "Home",
                                ),
                            ),
                            variant="surface",
                            size="3",
                            style=rx.style.Style({"cursor": "pointer"}),
                        ),
                        href="/",
                    ),
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("blocks"),
                                rx.text("Tools"),
                            ),
                            variant="surface",
                            size="3",
                            style=rx.style.Style({"cursor": "pointer"}),
                        ),
                        href="/tools",
                    ),
                    rx.popover.root(
                        rx.popover.trigger(
                            rx.button(
                                rx.icon("palette"),
                                variant="surface",
                                size="3",
                                style=rx.style.Style({"cursor": "pointer"}),
                            ),
                        ),
                        rx.popover.content(
                            rx.vstack(
                                rx.heading("Change theme"),
                                rx.grid(
                                    theme_button.theme_button(
                                        "red",
                                        "color(display-p3 0.659 0.298 0.297)",
                                        "rgba(23, 17, 17, 0.5)",
                                    ),
                                    theme_button.theme_button(
                                        "violet",
                                        "color(display-p3 0.417 0.341 0.784)",
                                        "rgba(20, 18, 30, 0.5)",
                                    ),
                                    theme_button.theme_button(
                                        "blue",
                                        "color(display-p3 0.247 0.556 0.969)",
                                        "rgba(15, 20, 30, 0.5)",
                                    ),
                                    theme_button.theme_button(
                                        "teal",
                                        "color(display-p3 0.297 0.637 0.581)",
                                        "rgba(15, 20, 20, 0.5)",
                                    ),
                                    theme_button.theme_button(
                                        "gold",
                                        "color(display-p3 0.579 0.517 0.41)",
                                        "rgba(18, 18, 18, 0.5)",
                                    ),
                                    spacing="3",
                                    columns="4",
                                ),
                            )
                        ),
                    ),
                    align="center",
                    spacing="3",
                    height="60px",
                )
            ),
            justify="between",
            padding_x="20px",
            height="60px",
            width="100vw",
            style=rx.style.Style(
                {
                    "position": "sticky",
                    "top": "0",
                    "z-index": "1000",
                    "background-color": GlobalState.theme_accent_navbar_color,
                    "box-shadow": "0 0 10px 0 rgba(0, 0, 0, 0.1)",
                    "backdrop-filter": "blur(20px)",
                }
            ),
        )
    )
