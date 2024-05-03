import reflex as rx


def banner() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.vstack(
                        rx.heading(
                            "Create an atractive",
                            size="9",
                            weight="bold",
                            style=rx.style.Style({"color": "var(--accent-9)"}),
                        ),
                        rx.heading(
                            "profile",
                            size="9",
                            weight="bold",
                            style=rx.style.Style({"color": "var(--accent-9)"}),
                        ),
                    ),
                    rx.text(
                        "This tool will help you to create a beautiful github profile."
                    ),
                    rx.box(height="20px"),
                    rx.link(
                        rx.button(
                            "Create profile README",
                            size="4",
                            color="primary",
                            style=rx.style.Style({"cursor": "pointer"}),
                        ),
                        href="/tools/readme/profile/create/",
                    ),
                ),
                rx.stack(
                    rx.icon(
                        "star",
                        size=200,
                        style=rx.style.Style({"color": "var(--accent-5)"}),
                    ),
                    rx.icon(
                        "star",
                        size=200,
                        style=rx.style.Style({"color": "var(--accent-6)"}),
                    ),
                    rx.icon(
                        "star",
                        size=200,
                        style=rx.style.Style({"color": "var(--accent-7)"}),
                    ),
                    rx.icon(
                        "star",
                        size=200,
                        style=rx.style.Style({"color": "var(--accent-8)"}),
                    ),
                    rx.icon(
                        "star",
                        size=200,
                        style=rx.style.Style({"color": "var(--accent-9)"}),
                    ),
                ),
                justify="between",
                width="100vw",
                padding_x="20px",
            ),
            align="start",
            justify="center",
            height="100vh",
            width="100vw",
        ),
    )
