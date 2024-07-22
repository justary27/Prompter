from django import forms

class PromptForm(forms.Form):
    MODEL_CHOICES = [
        ("gemini", "Gemini"),
        ("claude", "Claude"),
        ("phinde", "Phinde"),
    ]

    model = forms.ChoiceField(choices=MODEL_CHOICES)
    prompt = forms.CharField(widget=forms.Textarea)
