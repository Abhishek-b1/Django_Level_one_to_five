from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # Every details of list is saved because of ListView
    # Here the ListView is creating a school list and naming it school_list. In the school_list school is coming from
    # the .School, the ListView is lowering case of .School and renaming it as school_list which can be called in
    # school_list.html in for loop or for other manipulations.
    # Or if we want to change the default name then use context_object_name = "changed name" and this name can be
    # called in the school_list.html for further manipulation.


class SchoolDetailView(DetailView):    # Detail view returns model in the lower case.
    context_object_name = 'schools_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principle', 'location')    # Here creating the fields given in the parenthesis
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principle')    # Here we are updating name and principle of the school.
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")




