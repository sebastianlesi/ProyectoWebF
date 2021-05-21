
from django.contrib.auth.models import User
from django.test import TestCase
from era.models import Publicacion

class Publication(TestCase):
    def setUp(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")

        Publicacion.objects.create(name="Unknown Publication")

