import reflex as rx


def presentation_card(icon: str, heading: str, paragraph: str) -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.center(
                    rx.icon(
                        icon,
                        size=35,
                        stroke_width=1.5,
                        color="black",
                    ),
                ),
                justify="center",
                align="center",
                style=rx.style.Style(
                    {
                        "background_color": "var(--accent-9)",
                        "border-radius": "5px",
                    }
                ),
                height="50px",
                width="50px",
            ),
            rx.box(
                rx.heading(
                    heading,
                    size="5",
                    weight="bold",
                    style=rx.style.Style(
                        {
                            "color": "var(--accent-9)",
                            "margin-left": "10px",
                        }
                    ),
                ),
                rx.text(
                    paragraph,
                    style=rx.style.Style(
                        {
                            "color": "rgb(150, 150, 150)",
                            "margin-left": "10px",
                        }
                    ),
                ),
                width="200px",
            ),
        )
    )
