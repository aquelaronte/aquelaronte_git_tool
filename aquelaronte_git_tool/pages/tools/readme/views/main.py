import reflex as rx
from aquelaronte_git_tool.components import tool_card


def main() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    "README generator",
                    size="9",
                    weight="bold",
                    style=rx.style.Style({"color": "var(--accent-9)"}),
                ),
                rx.text("Choose a modality to generate a README file."),
                align="center",
                width="100vw",
            ),
            rx.grid(
                tool_card.tool_card(
                    "user",
                    "Profile README",
                    "Customize your profile README.",
                    "/tools/readme/profile",
                ),
                tool_card.tool_card(
                    "braces",
                    "Project README",
                    "Customize your project README.",
                    "/tools/readme/project",
                ),
                width="100vw",
                columns="5",
                justify="center",
                align="center",
                flow="row",
                spacing="6",
            ),
            height="100vh",
            width="100vw",
            padding_x="20px",
            spacing="9",
        ),
    )
