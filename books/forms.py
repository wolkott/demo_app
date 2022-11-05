from django import forms
from .models import Author, Book
from crispy_forms.helper import FormHelper,reverse


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'address', 'url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'price','author')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.render_required_fields = False
