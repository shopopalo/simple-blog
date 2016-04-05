from markdownx import forms
from markdownx.fields import MarkdownxFormField


class MyForm(forms.Form):
    myfield = MarkdownxFormField()
