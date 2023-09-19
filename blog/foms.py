from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(max_length=30, label="Your Name:",
                           widget=forms.TextInput(attrs={
                               "id": "name-id",
                           }))
    email = forms.EmailField(label="Email Address:",
                             widget=forms.EmailInput(attrs={
                                 "id": "email-id"
                             }))
    description = forms.CharField(max_length=150, label="Your comment:",
                                  widget=forms.Textarea(attrs={
                                      "id": "comment",
                                      "rows": 4
                                  }))
