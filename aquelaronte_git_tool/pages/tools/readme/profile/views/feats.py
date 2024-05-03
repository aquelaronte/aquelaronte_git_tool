import reflex as rx
from aquelaronte_git_tool.components.presentation_card import presentation_card


def feats() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading(
                "Features",
                size="9",
                weight="bold",
                style=rx.style.Style({"color": "var(--accent-9)"}),
            ),
            rx.hstack(
                rx.vstack(
                    presentation_card(
                        icon="computer",
                        heading="Tech stack",
                        paragraph="In AGTool you can create a profile with your tech stack and share it with others.",
                    ),
                    presentation_card(
                        icon="badge",
                        heading="Goals",
                        paragraph="You can share your goals to the world in your profile.",
                    ),
                    presentation_card(
                        icon="network",
                        heading="Connections",
                        paragraph="Connect with other developers sharing your tastes and interests.",
                    ),
                    spacing="6",
                ),
                rx.vstack(
                    presentation_card(
                        icon="heart",
                        heading="Community",
                        paragraph="Join the community and share your knowledge with others in your github profile README.",
                    ),
                    presentation_card(
                        icon="zap",
                        heading="Fast",
                        paragraph="Customize your profile in seconds with AGTool.",
                    ),
                    presentation_card(
                        icon="hand-heart",
                        heading="Aesthetical",
                        paragraph="Make your profile stand out with a beautiful design.",
                    ),
                    spacing="6",
                ),
                spacing="6",
            ),
            rx.box(height="50px"),
            rx.button(
                "Get started",
                size="4",
                variant="surface",
                style=rx.style.Style({"cursor": "pointer"}),
            ),
            justify="start",
            align="center",
            height="100vh",
            width="100vw",
            padding_x="20px",
        )
    )
