from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .apps import DetailsForm, DetailsModelForm

from .models import List
# Create your views here.

def index(request):
    return HttpResponse("<h1>Still working on it</h1>")

def detail(request):
    template = loader.get_template('form/index.html')
    return HttpResponse(template.render(request))

def home(request):
    #print request.POST["Name1"], request.POST["Color1"], request.POST["Animal1"]


    #DetailsForm App
    # detailform = DetailsForm(request.POST or None)
    #
    # if detailform.is_valid():
    #     name = detailform.cleaned_data['name']
    #     color = detailform.cleaned_data['color']
    #     animal = detailform.cleaned_data['cats_or_dogs']
    #
    #     new_data, created = List.objects.get_or_create(name=name, favorite_color=color, cats_or_dogs=animal)
    #     print new_data, created

    #DetailsModelFOrm App
    form = DetailsModelForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        # Do somthing here if required
        #
        # name = form.cleaned_data['name']
        # color = form.cleaned_data['favorite_color']
        # animal = form.cleaned_data['cats_or_dogs']
        #
        # add_details, created = List.objects.get_or_create(name=name, favorite_color=color, cats_or_dogs=animal)

        new_join.save()
        # If form data is submitted, reset the form
        form = DetailsModelForm()

    template = 'form/index.html'
    context = {"form": form}
    return render(request, template, context)
