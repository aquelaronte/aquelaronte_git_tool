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
                        icon="folder-git",
                        heading="Projects",
                        paragraph="In AGTool you can create your project docs. It could be an API, a website, or a mobile app.",
                    ),
                    presentation_card(
                        icon="code",
                        heading="Code",
                        paragraph="Show your code in your profile README. You can add code snippets, gists, and repositories.",
                    ),
                    presentation_card(
                        icon="smile",
                        heading="More easier",
                        paragraph="Make your profile README in a few clicks. No need to know markdown or HTML.",
                    ),
                    spacing="6",
                ),
                rx.vstack(
                    presentation_card(
                        icon="pencil",
                        heading="Customizable",
                        paragraph="With this tool you can have all required tools to make your profile README unique and beautiful.",
                    ),
                    presentation_card(
                        icon="users",
                        heading="Connect with others",
                        paragraph="Be social! Add your social media links to your profile README.",
                    ),
                    presentation_card(
                        icon="speech",
                        heading="Comunicate better",
                        paragraph="Add all your contact information to your profile README. Let others know how to reach you.",
                    ),
                    spacing="6",
                ),
                rx.vstack(
                    presentation_card(
                        icon="star",
                        heading="Professional",
                        paragraph="Make your personal and projects README look professional embedding it with your personal touch.",
                    ),
                    presentation_card(
                        icon="arrow-down-from-line",
                        heading="Download",
                        paragraph="Download your profile README as a markdown file and use it in your GitHub profile.",
                    ),
                    spacing="6",
                ),
                spacing="6",
            ),
            rx.box(height="50px"),
            justify="start",
            align="center",
            height="100vh",
            width="100vw",
            padding_x="20px",
        )
    )
