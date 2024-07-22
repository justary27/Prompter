from django.shortcuts import render
from .forms import PromptForm
from django.http import HttpResponse
from .utils import generate_schema

def index(request):
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            model = form.cleaned_data['model']
            prompt = form.cleaned_data['prompt']

            # Generate the schema
            schema = generate_schema(model, prompt)

            return render(request, 'website/result.html', {'schema': schema})
    else:
        form = PromptForm()

    return render(request, 'website/index.html', {'form': form})

