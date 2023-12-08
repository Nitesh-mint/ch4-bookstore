from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user  = User.objects.create(username="Nitesh", email="nitesh@gmail.com", password="testpass123")
        self.assertEqual(user.username ,"Nitesh")
        self.assertEqual(user.email ,"nitesh@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username="superuser", email="superuser@gmail.com", password="superuser123")
        self.assertEqual(admin_user.username, "superuser")
        self.assertEqual(admin_user.email, "superuser@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


