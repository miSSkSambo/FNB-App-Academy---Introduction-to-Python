import flet as ft


def main(page: ft.Page):
    page.title = "Two-View Greeting App"
    page.window.width = 450
    page.window.height = 520
    page.padding = 24

    # Keep the entered name in main so both views can use it.
    user_name = ""

    name_field = ft.TextField(
        label="Enter your name",
        hint_text="e.g. Katlego",
        width=320,
        autofocus=True,
    )

    def show_empty_name_dialog():
        dialog = ft.AlertDialog(
            title=ft.Text("Name required"),
            content=ft.Text("Please enter your name before continuing."),
        )
        page.show_dialog(dialog)

    async def continue_to_greeting(e):
        nonlocal user_name
        user_name = (name_field.value or "").strip()

        if not user_name:
            show_empty_name_dialog()
            return

        await page.push_route("/greeting")

    async def go_home(e):
        await page.push_route("/")

    def route_change(e):
        page.views.clear()

        if page.route == "/greeting":
            page.views.append(
                ft.View(
                    route="/greeting",
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(
                                    f"Hello, {user_name}!",
                                    size=28,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Button(
                                    content="Back",
                                    on_click=go_home,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=24,
                            expand=True,
                        )
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        else:
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(
                                    "Greeting App",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    "Enter your name to receive a greeting.",
                                    size=16,
                                ),
                                name_field,
                                ft.Button(
                                    content="Continue",
                                    on_click=continue_to_greeting,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=20,
                            expand=True,
                        )
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        page.update()

    page.on_route_change = route_change
    route_change(None)


if __name__ == "__main__":
    ft.run(main)
