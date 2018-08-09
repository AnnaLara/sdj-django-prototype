from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import JobListing


class ListingTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.jobListing = JobListing.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        jobListing = JobListing(title='A sample title')
        self.assertEqual(str(jobListing), jobListing.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.jobListing.get_absolute_url(), '/listing/'+str(self.jobListing.pk)+'/')

    def test_listing_content(self):
        self.assertEqual(f'{self.jobListing.title}', 'A good title')
        self.assertEqual(f'{self.jobListing.author}', 'testuser')
        self.assertEqual(f'{self.jobListing.body}', 'Nice body content')

    def test_listing_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_listing_detail_view(self):
        response = self.client.get('/listing/'+str(self.jobListing.pk)+'/')
        no_response = self.client.get('/listing/1000000000/')

        ##this test line fails for some reason:
        self.assertEqual(response.status_code, 200)
        ##

        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'listing_detail.html')

    def test_new_listing_view(self):
        response = self.client.post(reverse('post-new-listing'), {
            'title': 'New title',
            'body': 'New text',
            'user': self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_edit_listing_view(self):
        jobListing = JobListing.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

        jobListing.pk

        response = self.client.post(reverse('edit-listing', args=str(jobListing.pk)), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)

    def test_delete_listing_view(self):
        response = self.client.get(reverse('delete-listing', args='1'))
        self.assertEqual(response.status_code, 200)
