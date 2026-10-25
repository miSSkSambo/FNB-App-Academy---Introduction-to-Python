
import flet as ft


def main(page: ft.Page):
    page.title = "Greeting App"
    page.window.width = 420
    page.window.height = 420
    page.padding = 30
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    name_field = ft.TextField(
        label="Enter your name",
        hint_text="e.g. Katlego",
        width=320,
        autofocus=True,
    )

    greeting_text = ft.Text(
        "Your greeting will appear here.",
        size=20,
        weight=ft.FontWeight.BOLD,
    )

    def greet_me(e):
        name = name_field.value.strip() if name_field.value else ""

        if name:
            greeting_text.value = f"Hello, {name}!"
        else:
            greeting_text.value = "Please enter your name."

        page.update()

    greet_button = ft.Button(
        content="Greet Me",
        on_click=greet_me,
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Greeting App",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                ),
                name_field,
                greet_button,
                greeting_text,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    ft.run(main)
