import reflex as rx


def foot() -> rx.Component:
    return rx.fragment(
        rx.box(
            rx.hstack(
                rx.hstack(
                    rx.heading("AGTool", size="9", weight="bold"),
                    rx.icon("github", size=60),
                    justify="center",
                    align="center",
                    height="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Made by ",
                        rx.link(
                            "Aquelaronte",
                            is_external=True,
                            href="https://github.com/aquelaronte/",
                        ),
                    ),
                    rx.text(
                        "Made with ",
                        rx.link(
                            "Reflex",
                            is_external=True,
                            href="https://reflex.dev/",
                        ),
                    ),
                    rx.text(
                        "Source code on ",
                        rx.link(
                            "GitHub",
                            is_external=True,
                            href="https://github.com/aquelaronte/aquelaronte_git_tool",
                        ),
                    ),
                    justify="center",
                    align="center",
                    height="100%",
                ),
                justify="between",
                align="center",
                height="100%",
            ),
            style=rx.style.Style(
                {
                    "padding": "100px 200px",
                    "width": "100vw",
                    "height": "100px",
                    "background": "var(--slate-2)",
                }
            ),
        )
    )
