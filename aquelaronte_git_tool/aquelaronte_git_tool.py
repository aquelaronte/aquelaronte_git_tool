import reflex as rx
from .pages.router import load_pages

app = rx.App()
app.stylesheets.append(
    "https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"
)
app.style = {
    rx.text: {"font_family": "Roboto, sans-serif"},
    rx.heading: {"font_family": "Roboto, sans-serif"},
}

load_pages(app)
