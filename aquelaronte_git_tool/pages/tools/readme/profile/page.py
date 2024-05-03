import reflex as rx
import aquelaronte_git_tool.components.navbar as navbar
from .views import banner, feats


def page() -> rx.Component:
    return rx.vstack(
        navbar.navbar(),
        banner.banner(),
        feats.feats(),
        align="start",
        justify="start",
    )
