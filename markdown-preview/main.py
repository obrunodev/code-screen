import flet as ft


def main(page: ft.Page):
    # page.window_width = 540
    # page.window_height = 960
    page.theme_mode = "dark"
    page.title = "Markdown preview"
    page.appbar = ft.AppBar(
        title=ft.Text("Markdown Preview"),
        center_title=True,
        bgcolor=ft.colors.BLUE,
    )

    def update_preview(e):
        """
        Updates the RHS(markdown/preview) when the content of the textfield changes.
        :param e: the event that triggered the function
        """
        md.value = text_field.value
        page.update()

    text_field = ft.TextField(
        value="Um texto de teste",  # the initial value in the field (a simple Markdown code to test)
        multiline=True,  # True means: it will be possible to have many lines of text
        expand=True,  # tells the field to 'expand' (take all the available space)
        border_color=ft.colors.TRANSPARENT, # makes the border of the field transparent(invisible), creating an immersive effect
        on_change=update_preview,
    )
    md = ft.Markdown(
        value=text_field.value,  # make its value be equal to the content of our text_field
        selectable=True,  # to make the rendered markdown selectable
        extension_set="gitHubWeb",
        on_tap_link=lambda e: page.launch_url(e.data)  # what happens when a link is clicked: a browser tab is opened up, with the link's URL
    )

    page.add(
        ft.Row(  # we use the row here, so everything fits on a line
            controls=[
                text_field,
                ft.VerticalDivider(color=ft.colors.WHITE),
                ft.Container(  # we use the container here, to take advantage of its content alignment property
                    ft.Column(  # we use the column here, to take advantage of its scroll property
                        [md],
                        scroll="hidden",  # we make the Markdown scrollable
                    ),
                    expand=True,  # we make it fill up all the available space
                    alignment=ft.alignment.top_left,  # align the column
                )
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
            expand=True,  # we make it fill up all the available space
        )  # a row containing our text_field on the LHS and Markdown on the RHS
    )


ft.app(main)