import reflex as rx
from ..state import ProjectState


def header() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading(
                "Input your headers for your project",
                size="6",
                weight="bold",
                style=rx.style.Style({"color": "var(--accent-9)"}),
            ),
            rx.box(height="25px"),
            rx.input.root(
                rx.input.slot(rx.icon("folder-git")),
                rx.input.input(
                    placeholder="Enter your github project name",
                    tab_index=1,
                    on_change=ProjectState.set_project_name,
                ),
                size="3",
                style=rx.style.Style(
                    {"width": "60%"},
                ),
            ),
            rx.box(height="30px"),
            rx.input.root(
                rx.input.slot(rx.icon("user")),
                rx.input.input(
                    placeholder="Enter your github username",
                    tab_index=1,
                    on_change=ProjectState.set_github_username,
                ),
                size="3",
                style=rx.style.Style(
                    {"width": "60%"},
                ),
            ),
            rx.input.root(
                rx.input.slot(rx.icon("github")),
                rx.input.input(
                    placeholder="Enter your github repository name",
                    tab_index=1,
                    on_change=ProjectState.set_repository_name,
                ),
                size="3",
                style=rx.style.Style(
                    {"width": "60%"},
                ),
            ),
            rx.button(
                "Done",
                on_click=ProjectState.fetch_headers,
                style=rx.style.Style(
                    {
                        "width": "60%",
                        "cursor": "pointer",
                    },
                ),
            ),
            rx.cond(
                ProjectState.headers_list != [],
                rx.hstack(
                    rx.foreach(
                        ProjectState.headers_list,
                        lambda header: rx.image(src=header["badge"]),
                    ),
                ),
            ),
            rx.box(height="10px"),
            rx.hstack(
                rx.button(
                    rx.hstack(
                        rx.icon(
                            "arrow-left",
                            style=rx.style.Style({"color": "var(--accent-9)"}),
                        ),
                        rx.text("Back"),
                    ),
                    style=rx.style.Style({"cursor": "pointer"}),
                    variant="outline",
                    on_click=lambda: ProjectState.set_tab_value("1"),
                    tab_index=5,
                ),
                rx.button(
                    rx.hstack(
                        rx.text("Next"),
                        rx.icon(
                            "arrow-right",
                            style=rx.style.Style({"color": "var(--accent-9)"}),
                        ),
                    ),
                    style=rx.style.Style({"cursor": "pointer"}),
                    variant="outline",
                    on_click=lambda: ProjectState.submit_headers(),
                    tab_index=5,
                ),
            ),
            align="center",
            padding_y="26px",
            width="100vw",
        )
    )
