import reflex as rx
from .index.page import page as index_page
from .tools.page import page as tools_page
from .tools.readme.page import page as tools_readme_page
from .tools.readme.profile.page import page as tools_readme_profile_page
from .tools.readme.profile.create.page import page as tools_readme_profile_create_page
from .tools.readme.project.page import page as tools_readme_project_page
from .tools.readme.project.create.page import page as tools_readme_project_create_page
from .global_state import GlobalState


def load_pages(app: rx.App) -> None:
    def load_page(page, route: str, title: str) -> None:
        def page_theme() -> rx.Component:
            return rx.theme(
                page(),
                appearance=GlobalState.theme_appeareance,
                accent_color=GlobalState.theme_accent_color,
            )

        app.add_page(page_theme, route=route, title=title, image="favicon.ico")
        print(f"✅ Loaded page {route}")

    load_page(index_page, "/", "AGTool | Home")
    load_page(tools_page, "/tools", "AGTool | Tools")
    load_page(tools_readme_page, "/tools/readme", "AGTool | Tools | Readme")
    load_page(
        tools_readme_profile_page,
        "/tools/readme/profile",
        "AGTool | Tools | Readme | Profile",
    )
    load_page(
        tools_readme_project_page,
        "/tools/readme/project",
        "AGTool | Tools | Readme | Project",
    ),
    load_page(
        tools_readme_profile_create_page,
        "/tools/readme/profile/create",
        "AGTool | Tools | Readme | Profile | Create",
    )
    load_page(
        tools_readme_project_create_page,
        "/tools/readme/project/create",
        "AGTool | Tools | Readme | Project | Create",
    )
