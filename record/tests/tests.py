from django.test import TestCase
from django.urls import resolve
from record.models import *


class ModelTestCase(TestCase):

    def setUp(self):
        soft_job = Category.objects.create(name="Soft_job")
        lol = Category.objects.create(name="LoL")
        westdoor = KeyWord.objects.create(name="westdoor")
        
    def test_category_auto_create_url(self):
        soft_job = Category.objects.get(name="Soft_job")
        lol = Category.objects.get(name="LoL")
        self.assertEqual(soft_job.url, 'https://www.ptt.cc/bbs/' + soft_job.name + "/index.html")
        self.assertEqual(lol.url, 'https://www.ptt.cc/bbs/' + lol.name + "/index.html")

    def test_key_has_more_than_one_category(self):
        soft_job = Category.objects.get(name="Soft_job")
        lol = Category.objects.get(name="LoL")
        westdoor = KeyWord.objects.get(name="westdoor")
        westdoor.category.add(soft_job)
        westdoor.category.add(lol)
        self.assertIn(soft_job, westdoor.category.all())
        self.assertIn(lol, westdoor.category.all())