import reflex as rx
import aquelaronte_git_tool.components.navbar as navbar
from .views import banner, feats, foot


def page() -> rx.Component:
    return rx.vstack(
        navbar.navbar(),
        banner.banner(),
        feats.feats(),
        foot.foot(),
        align="start",
        justify="start",
    )
