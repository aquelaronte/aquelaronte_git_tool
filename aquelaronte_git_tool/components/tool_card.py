import reflex as rx


def tool_card(icon: str, heading: str, description: str, href: str) -> rx.Component:
    return rx.fragment(
        rx.card(
            rx.link(
                rx.vstack(
                    rx.box(height="30px"),
                    rx.icon(
                        icon,
                        size=60,
                    ),
                    rx.box(height="30px"),
                    rx.heading(
                        heading,
                        size="7",
                        weight="bold",
                        style=rx.style.Style({"color": "var(--accent-9)"}),
                    ),
                    rx.text(
                        description,
                        style=rx.style.Style(
                            {
                                "color": "var(--accent-9-contrast)",
                                "font-size": "0.8rem",
                                "text-align": "center",
                            }
                        ),
                    ),
                    spacing="2",
                    justify="center",
                    align="center",
                ),
                href=href,
                style=rx.style.Style({"border": "none", "text-decoration": "none"}),
            ),
        )
    )
