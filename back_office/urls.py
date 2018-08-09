from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListingListView.as_view(), name='home'),
    path('listing/<int:pk>/', views.ListingDetailView.as_view(), name='listing-detail'),
    path('new-listing/', views.NewListingView.as_view(), name='post-new-listing'),
    path('edit-listing/<int:pk>', views.EditListingView.as_view(), name='edit-listing'),
    path('delete-listing/<int:pk>', views.DeleteListingView.as_view(), name='delete-listing'),
]
