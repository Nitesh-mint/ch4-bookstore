from django.urls import reverse, resolve
from django.test import SimpleTestCase

from .views import HomePageView, AboutPageView

class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.assertEqual(self.response.status_code,200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")
    
    def test_homepage_contains_correct_home(self):
        self.assertContains(self.response, "homepage")
    
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "This should not be on the page!")

class AboutPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, "about.html")
    
    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response,"About")
    
    def test_aboutpage_doesnot_contain_incorrect_html(self):
        self.assertNotContains(self.response, "HI! THis should not be here!")

    def test_aboutpage_url_resolves_abougepageview(self):
        view = resolve("/about/")
        self.assertEqual(
            view.func.__name__, 
            AboutPageView.as_view().__name__
        )
                            


        
