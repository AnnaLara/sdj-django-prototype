from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from . models import JobListing

class ListingListView(ListView):
    template_name = 'home.html'
    model = JobListing

class ListingDetailView(DetailView):
    model = JobListing
    template_name = 'listing_detail.html'

class NewListingView(CreateView):
    model = JobListing
    template_name = 'new_listing.html'
    fields = '__all__'

class EditListingView(UpdateView):
    model = JobListing
    template_name = 'edit_listing.html'
    fields = ['title', 'body']

class DeleteListingView(DeleteView):
    model = JobListing
    template_name = 'delete_listing.html'
    success_url = reverse_lazy('home')
