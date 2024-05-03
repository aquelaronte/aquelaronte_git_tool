import reflex as rx


class GlobalState(rx.State):
    theme_appeareance: str = "dark"
    theme_accent_color: str = "red"
    theme_accent_navbar_color: str = "rgba(23, 17, 17, 0.5)"

    def change_accent(self, accent: str, navbar_color: str) -> None:
        self.theme_accent_color = accent
        self.theme_accent_navbar_color = navbar_color
