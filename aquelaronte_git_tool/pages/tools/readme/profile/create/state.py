from env import Environment
import reflex as rx
import requests


class State(rx.State):
    # Tab
    tab_value: str = "1"

    def set_tab_value(self, value: str):
        self.tab_value = value

    # Tastes
    tastes: list = ["", "", "", ""]
    tastes_markdown: str = ""

    def set_first_taste(self, value):
        self.tastes[0] = value

    def set_second_taste(self, value):
        self.tastes[1] = value

    def set_third_taste(self, value):
        self.tastes[2] = value

    def set_fourth_taste(self, value):
        self.tastes[3] = value

    def submit_tastes(self):
        self.set_tastes_markdown()
        self.set_tab_value("2")

    def set_tastes_markdown(self):
        value = f"""# ❗️ Tastes\n🔭 {self.tastes[0]}<br>\n🌱 {self.tastes[1]}<br>\n💬 {self.tastes[2]}<br>\n👯 {self.tastes[3]}<br>\n"""
        self.tastes_markdown = value
        self.markdown_list[0] = value
        self.set_preview_markdown()

    # Tech Stack
    tech_stack_languages: list[dict] = [
        {
            "name": "Python",
            "icon": r"https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54",
            "selected": False,
        },
        {
            "name": "Java",
            "icon": r"https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=whit",
            "selected": False,
        },
        {
            "name": "JS",
            "icon": r"https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E",
            "selected": False,
        },
        {
            "name": "C",
            "icon": r"https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white",
            "selected": False,
        },
        {
            "name": "C++",
            "icon": r"https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white",
            "selected": False,
        },
        {
            "name": "C#",
            "icon": r"https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=csharp&logoColor=white",
            "selected": False,
        },
        {
            "name": "Swift",
            "icon": r"https://img.shields.io/badge/swift-F54A2A?style=for-the-badge&logo=swift&logoColor=white",
            "selected": False,
        },
        {
            "name": "Ruby",
            "icon": r"https://img.shields.io/badge/ruby-%23CC342D.svg?style=for-the-badge&logo=ruby&logoColor=white",
            "selected": False,
        },
        {
            "name": "PHP",
            "icon": r"https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white",
            "selected": False,
        },
        {
            "name": "Go",
            "icon": r"https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white",
            "selected": False,
        },
        {
            "name": "Rust",
            "icon": r"https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white",
            "selected": False,
        },
        {
            "name": "TS",
            "icon": r"https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white",
            "selected": False,
        },
        {
            "name": "Kotlin",
            "icon": r"https://img.shields.io/badge/kotlin-%237F52FF.svg?style=for-the-badge&logo=kotlin&logoColor=white",
            "selected": False,
        },
        {
            "name": "Scala",
            "icon": r"https://img.shields.io/badge/scala-%23DC322F.svg?style=for-the-badge&logo=scala&logoColor=white",
            "selected": False,
        },
        {
            "name": "Perl",
            "icon": r"https://img.shields.io/badge/perl-%2339457E.svg?style=for-the-badge&logo=perl&logoColor=white",
            "selected": False,
        },
        {
            "name": "R",
            "icon": r"https://img.shields.io/badge/r-%23276DC3.svg?style=for-the-badge&logo=r&logoColor=white",
            "selected": False,
        },
        {
            "name": "Lua",
            "icon": r"https://img.shields.io/badge/lua-%232C2D72.svg?style=for-the-badge&logo=lua&logoColor=white",
            "selected": False,
        },
        {
            "name": "Haskell",
            "icon": r"https://img.shields.io/badge/Haskell-5e5086?style=for-the-badge&logo=haskell&logoColor=white",
            "selected": False,
        },
        {
            "name": "Dart",
            "icon": r"https://img.shields.io/badge/dart-%230175C2.svg?style=for-the-badge&logo=dart&logoColor=white",
            "selected": False,
        },
    ]

    tech_stack_frameworks: list[dict] = [
        {
            "name": "DJango",
            "icon": r"https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white",
            "selected": False,
        },
        {
            "name": "Flask",
            "icon": r"https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white",
            "selected": False,
        },
        {
            "name": "React",
            "icon": r"https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB",
            "selected": False,
        },
        {
            "name": "Angular",
            "icon": r"https://img.shields.io/badge/angular-%23DD0031.svg?style=for-the-badge&logo=angular&logoColor=white",
            "selected": False,
        },
        {
            "name": "Vue.js",
            "icon": r"https://img.shields.io/badge/vue.js-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D",
            "selected": False,
        },
        {
            "name": "Express",
            "icon": r"https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB",
            "selected": False,
        },
        {
            "name": "Spring",
            "icon": r"https://img.shields.io/badge/spring-%236DB33F.svg?style=for-the-badge&logo=spring&logoColor=white",
            "selected": False,
        },
        {
            "name": "Rails",
            "icon": r"https://img.shields.io/badge/rails-%23CC0000.svg?style=for-the-badge&logo=ruby-on-rails&logoColor=white",
            "selected": False,
        },
        {
            "name": "Laravel",
            "icon": r"https://img.shields.io/badge/laravel-%23FF2D20.svg?style=for-the-badge&logo=laravel&logoColor=white",
            "selected": False,
        },
        {
            "name": ".NET",
            "icon": r"https://img.shields.io/badge/.NET-5C2D91?style=for-the-badge&logo=.net&logoColor=white",
            "selected": False,
        },
        {
            "name": "Flutter",
            "icon": r"https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white",
            "selected": False,
        },
        {
            "name": "Native",
            "icon": r"https://img.shields.io/badge/react_native-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB",
            "selected": False,
        },
        {
            "name": "Xamarin",
            "icon": r"https://img.shields.io/badge/Xamarin-3199DC?style=for-the-badge&logo=xamarin&logoColor=white",
            "selected": False,
        },
        {
            "name": "Electron",
            "icon": r"https://img.shields.io/badge/Electron-191970?style=for-the-badge&logo=Electron&logoColor=white",
            "selected": False,
        },
        {
            "name": "Nest.js",
            "icon": r"https://img.shields.io/badge/nestjs-%23E0234E.svg?style=for-the-badge&logo=nestjs&logoColor=white",
            "selected": False,
        },
        {
            "name": "Ember.js",
            "icon": r"https://img.shields.io/badge/ember-1C1E24?style=for-the-badge&logo=ember.js&logoColor=#D04A37",
            "selected": False,
        },
        {
            "name": "Next.js",
            "icon": r"https://img.shields.io/badge/Next-black?style=for-the-badge&logo=next.js&logoColor=white",
            "selected": False,
        },
        {
            "name": "Nuxt.js",
            "icon": r"https://img.shields.io/badge/Nuxt-002E3B?style=for-the-badge&logo=nuxt.js&logoColor=#00DC82",
            "selected": False,
        },
        {
            "name": "FastAPI",
            "icon": r"https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi",
            "selected": False,
        },
    ]

    tech_stack_selected: list[dict] = []
    tech_stack_markdown: str = ""

    def submit_tech_stack(self):
        self.set_tech_stack_markdown()
        self.set_tab_value("3")

    def append_tech_stack(self, tech_stack: dict):
        for index, tech in enumerate(self.tech_stack_languages):
            if tech.get("name") == tech_stack.get("name"):
                self.tech_stack_languages[index]["selected"] = True
                break

        for index, tech in enumerate(self.tech_stack_frameworks):
            if tech.get("name") == tech_stack.get("name"):
                self.tech_stack_frameworks[index]["selected"] = True
                break
        
        value = tech_stack.copy()
        value["selected"] = True
        self.tech_stack_selected.append(value)

    def remove_tech_stack(self, tech_stack):
        for tech in self.tech_stack_selected:
            if tech.get("name") == tech_stack.get("name"):
                self.tech_stack_selected.remove(tech)
                break

        for index, tech in enumerate(self.tech_stack_languages):
            if tech.get("name") == tech_stack.get("name"):
                self.tech_stack_languages[index]["selected"] = False
                break

        for index, tech in enumerate(self.tech_stack_frameworks):
            if tech.get("name") == tech_stack.get("name"):
                self.tech_stack_frameworks[index]["selected"] = False
                break

    def submit_tech_stack(self):
        self.set_tech_stack_markdown()
        self.set_tab_value("3")

    def set_tech_stack_markdown(self):
        value = f"""# 🛠 Tech Stack \n"""
        for tech in self.tech_stack_selected:
            value += f"![{tech.get("name")}]({tech.get("icon")}) "

        self.tech_stack_markdown = value
        self.markdown_list[1] = value
        self.set_preview_markdown()
    
    # Stats
    stats: list[str] = ["", "", ""]
    stats_markdown: str = ""
    stats_error = False
    stats_loading = False
    stats_have_data = False
    username : str = ""


    def set_username(self, value):
        self.username = value

    def handle_enter(self, value):
        if value == "Enter":
            self.set_stats()

    def set_stats(self):
        self.stats_have_data = False
        self.stats_loading = True
        response = requests.get(f"https://api.github.com/users/{self.username}", headers={"Accept": "application/vnd.github.v3+json", "Authorization" : f"Bearer {Environment.github_token.value}"})
        self.stats_loading = False

        if response.status_code == 404:
            self.stats_error = True
            return

        self.stats[0] = f"https://github-readme-stats.vercel.app/api?username={self.username}&theme=dark&hide_border=false&include_all_commits=false&count_private=false"
        self.stats[1] = f"https://github-readme-streak-stats.herokuapp.com/?user={self.username}&theme=dark&hide_border=false"
        self.stats[2] = f"https://github-readme-stats.vercel.app/api/top-langs/?username={self.username}&theme=dark&hide_border=false&include_all_commits=false&count_private=false&layout=compact"
        self.stats_have_data = True

    def submit_stats(self):
        self.set_stats_markdown()
        self.set_tab_value("4")

    def set_stats_markdown(self):
        value = f"""\n # ⚡️ Stats \n![]({self.stats[0]})<br/> \n![]({self.stats[1]})<br/> \n![]({self.stats[2]})<br/>"""

        self.stats_markdown = value
        self.markdown_list[2] = value
        self.set_preview_markdown()

    # Contacts
    contacts: list = ["", "", "", ""]
    contact_markdown: str = ""

    def set_first_contact(self, value):
        self.contacts[0] = value

    def set_second_contact(self, value):
        self.contacts[1] = value

    def set_third_contact(self, value):
        self.contacts[2] = value

    def set_fourth_contact(self, value):
        self.contacts[3] = value

    def submit_contacts(self):
        self.set_contact_markdown()
        self.set_tab_value("5")

    def set_contact_markdown(self):
        value = f"""\n # 📫 Contact \nphone: {self.contacts[0]}<br/>\n instagram: {self.contacts[1]}<br/>\n linkedin: {self.contacts[2]}<br/>\n codepen: {self.contacts[3]}<br/>"""
        self.contact_markdown = value
        self.markdown_list[3] = value
        self.set_preview_markdown()

    # Markdown
    markdown_list: list = ["", "", "", ""]

    # Markdown Preview
    preview_markdown: str = ""

    def set_preview_markdown(self):
        self.preview_markdown = "".join(self.markdown_list)

    def download_file(self):
        return rx.download(data=self.preview_markdown.encode(), filename="README.md", )
