import reflex as rx


class ProjectState(rx.State):
    # Tabs
    tab_value: str = "1"

    def set_tab_value(self, value: str):
        self.tab_value = value

    # type
    project_type: str = ""

    def set_project_type(self, value: str):
        self.project_type = value
        self.set_tab_value("2")

    # headers
    project_name: str = ""

    github_username: str = ""
    repository_name: str = ""

    headers_list: list[dict] = []
    headers_markdown: str = ""

    def set_project_name(self, value: str):
        self.project_name = value

    def set_github_username(self, value: str):
        self.github_username = value

    def set_repository_name(self, value: str):
        self.repository_name = value

    def fetch_headers(self):
        self.headers_list = [
            {
                "name": "Top Language",
                "badge": f"https://img.shields.io/github/languages/top/{self.github_username}/{self.repository_name}?style=for-the-badge&color=%2300AABB",
            },
            {
                "name": "Forks",
                "badge": f"https://img.shields.io/github/forks/{self.github_username}/{self.repository_name}?style=for-the-badge&color=%23AA0067",
            },
            {
                "name": "Stars",
                "badge": f"https://img.shields.io/github/stars/{self.github_username}/{self.repository_name}?style=for-the-badge&color=%23ffff00",
            },
        ]

    def set_headers_markdown(self):
        value = ""
        for header in self.headers_list:
            value += f"![{header['name']}]({header['badge']}) "

        self.headers_markdown = f"# {self.project_name}\n{value}"
        self.markdown_list[0] = self.headers_markdown
        self.set_preview_markdown()

    def submit_headers(self):
        self.set_headers_markdown()
        self.set_tab_value("3")

    # description
    description_list: list = ["", "", "", ""]

    def set_first_description(self, value):
        self.description_list[0] = value

    def set_second_description(self, value):
        self.description_list[1] = value

    def set_description_markdown(self):
        self.description_markdown = f"\n## About\n{self.description_list[0]}\n ## Why {self.project_name}\n {self.description_list[1]}"
        self.markdown_list[1] = self.description_markdown
        self.set_preview_markdown()

    def submit_description(self):
        self.set_description_markdown()
        self.set_tab_value("4")

    # guides
    guides_list: list[dict] = []

    def append_guide(self, type: str, language: str):
        value = {
            "index": len(self.guides_list),
            "title": "",
            "type": type,
            "value": "",
            "language": language,
        }

        self.guides_list.append(value)

    def detach_guide(self, index: int):
        self.guides_list.pop(index)

    def update_guide_title(self, value, index):
        self.guides_list[index]["title"] = value

    def update_guide(self, value, index):
        self.guides_list[index]["value"] = value

    def set_guides_markdown(self):
        if self.guides_list != []:
            value = "# guides \n"
            for guide in self.guides_list:
                value += f"\n## {guide['title']}\n"
                if guide["type"] == "code":
                    value += f"\n```{guide['language']}\n{guide['value']}\n```\n"

                if guide["type"] == "text":
                    value += f"\n{guide['value']}\n"

            self.guides_markdown = value
            self.markdown_list[2] = self.guides_markdown

            self.set_preview_markdown()

    def submit_guides(self):
        self.set_guides_markdown()
        self.set_tab_value("5")

    # markdown
    markdown_list: str = [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ]

    # preview markdown
    preview_markdown: str = ""

    def set_preview_markdown(self):
        self.preview_markdown = "".join(self.markdown_list)

    def download_file(self):
        return rx.download(
            data=self.preview_markdown.encode(),
            filename="README.md",
        )
