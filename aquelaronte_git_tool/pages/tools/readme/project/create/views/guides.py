import reflex as rx
from ..state import ProjectState


def guides() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading(
                "Input your guides for your project (optional)",
                size="6",
                weight="bold",
                style=rx.style.Style({"color": "var(--accent-9)"}),
            ),
            rx.box(height="25px"),
            rx.foreach(
                ProjectState.guides_list,
                lambda guide: rx.vstack(
                    rx.hstack(
                        rx.button(
                            rx.icon("trash-2"),
                            on_click=lambda: ProjectState.detach_guide(guide["index"]),
                        ),
                        rx.input(
                            placeholder="Guide title",
                            style=rx.style.Style({"width": "60%"}),
                            on_change=lambda value: ProjectState.update_guide_title(
                                value, guide["index"]
                            ),
                        ),
                    ),
                    rx.text_area(
                        placeholder="Paste your guide here",
                        style=rx.style.Style({"width": "60%", "height": "200px"}),
                        on_change=lambda value: ProjectState.update_guide(
                            value, guide["index"]
                        ),
                    ),
                    align="center",
                    spacing="4",
                    width="100vw",
                    padding_bottom="20px",
                ),
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.icon("plus"),
                        rx.text("Add a guide"),
                        style=rx.style.Style({"width": "60%", "cursor": "pointer"}),
                    ),
                ),
                rx.menu.content(
                    rx.menu.item(
                        "Text",
                        on_click=lambda: ProjectState.append_guide("text", "None"),
                    ),
                    rx.menu.sub(
                        rx.menu.sub_trigger("Code"),
                        rx.menu.sub_content(
                            rx.menu.item(
                                "Python",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "python"
                                ),
                            ),
                            rx.menu.item(
                                "Javascript",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "javascript"
                                ),
                            ),
                            rx.menu.item(
                                "Typescript",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "typescript"
                                ),
                            ),
                            rx.menu.item(
                                "HTML",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "html"
                                ),
                            ),
                            rx.menu.item(
                                "CSS",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "css"
                                ),
                            ),
                            rx.menu.item(
                                "Java",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "java"
                                ),
                            ),
                            rx.menu.item(
                                "C",
                                on_click=lambda: ProjectState.append_guide("code", "c"),
                            ),
                            rx.menu.item(
                                "C++",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "c++"
                                ),
                            ),
                            rx.menu.item(
                                "C#",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "c#"
                                ),
                            ),
                            rx.menu.item(
                                "Rust",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "rust"
                                ),
                            ),
                            rx.menu.item(
                                "Go",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "go"
                                ),
                            ),
                            rx.menu.item(
                                "Ruby",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "ruby"
                                ),
                            ),
                            rx.menu.item(
                                "Swift",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "swift"
                                ),
                            ),
                            rx.menu.item(
                                "Kotlin",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "kotlin"
                                ),
                            ),
                            rx.menu.item(
                                "Bash",
                                on_click=lambda: ProjectState.append_guide(
                                    "code", "bash"
                                ),
                            ),
                        ),
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
                    on_click=lambda: ProjectState.set_tab_value("3"),
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
                    on_click=lambda: ProjectState.submit_guides(),
                    tab_index=5,
                ),
            ),
            align="center",
            padding_y="26px",
            width="100vw",
        ),
    )
