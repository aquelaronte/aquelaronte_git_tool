import reflex as rx

from aquelaronte_git_tool.components import tool_card


def main() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    "Tools",
                    size="9",
                    weight="bold",
                    style=rx.style.Style({"color": "var(--accent-9)"}),
                ),
                rx.text("Choose a tool to get started"),
                align="center",
                width="100vw",
            ),
            rx.grid(
                tool_card.tool_card(
                    "book-open",
                    "README generator",
                    "Generate a README file for your project or profile.",
                    "/tools/readme/",
                ),
                width="100vw",
                columns="5",
                justify="center",
                align="center",
                flow="row",
                as_child=True,
            ),
            height="100vh",
            width="100vw",
            padding_x="20px",
            spacing="9",
        ),
    )
