import reflex as rx


def banner() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.vstack(
                        rx.heading(
                            "AGTool helps you to",
                            size="9",
                            weight="bold",
                            style=rx.style.Style({"color": "var(--accent-9)"}),
                        ),
                        rx.heading(
                            "manage your github docs",
                            size="9",
                            weight="bold",
                            style=rx.style.Style({"color": "var(--accent-9)"}),
                        ),
                    ),
                    rx.text(
                        "Create, edit, and manage your github docs with AGTool. It's easy and fast.",
                    ),
                    rx.box(height="50px"),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "Get started",
                                size="4",
                                style=rx.style.Style({"cursor": "pointer"}),
                            ),
                            href="/tools",
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon("github", size=20, stroke_width=2),
                                    "View on Github",
                                    align="center",
                                ),
                                size="4",
                                style=rx.style.Style({"cursor": "pointer"}),
                            ),
                            is_external=True,
                            href="https://github.com/aquelaronte/aquelaronte_git_tool",
                        ),
                        spacing="3",
                    ),
                ),
                rx.stack(
                    rx.icon(
                        "sparkles",
                        size=350,
                        stroke_width=1,
                        class_name="animate-pulse",
                        style=rx.style.Style(
                            {
                                "color": "var(--accent-9-contrast)",
                                "position": "absolute",
                                "transform": "rotate(90deg)",
                            }
                        ),
                    ),
                    style=rx.style.Style(
                        {
                            "width": "auto",
                            "align_items": "center",
                            "justify_content": "center",
                            "flex-grow": "1",
                            "position": "relative",
                        }
                    ),
                ),
                justify="between",
                align="center",
                width="100vw",
                padding_x="20px",
            ),
            align="start",
            justify="center",
            height="100vh",
            width="100vw",
        ),
    )
