import flet as ft
from dropwise.loops import create_loop


def toggle_loop(loop):
    loop["completed"] = not loop["completed"]


def app(page: ft.Page):
    loops = []

    text_input = ft.TextField(label="What is on your mind?")
    create_button = ft.Button("Create Loop")
    loop_output = ft.Column()

    def create_loop_click(e):
        loop = create_loop(text_input.value)
        loops.append(loop)

        loop_button = ft.Button(
            f'{"🌕" if loop["completed"] else "🌑"} {loop["title"]}'
        )

        def toggle_this_loop(e):
            toggle_loop(loop)
            loop_button.content = (
                f'{"🌕" if loop["completed"] else "🌑"} {loop["title"]}'
            )
            page.update()

        loop_button.on_click = toggle_this_loop

        loop_output.controls.append(loop_button)
        page.update()

    create_button.on_click = create_loop_click

    page.add(
        ft.Text("Welcome to DropWise"),
        text_input,
        create_button,
        loop_output,
    )


if __name__ == "__main__":
    ft.run(app)