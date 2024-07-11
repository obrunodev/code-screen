import flet as ft


def main(page: ft.Page):
    page.title = "Code screen by Pythonista"
    page.window_width = 540
    page.window_height = 960
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    editor_html = """
    <div id="editor" style="height:100%; width:100%;"></div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.0/codemirror.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.0/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.0/mode/python/python.min.js"></script>
    <script>
        var editor = CodeMirror(document.getElementById('editor'), {
            mode: 'python',
            lineNumbers: true,
            theme: 'default'
        });
    </script>
    """

    editor = ft.Html(content=editor_html, expand=True)

    page.add(editor)


ft.app(main)