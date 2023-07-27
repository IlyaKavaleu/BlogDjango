from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
from learning_logs.models import Section, Model


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse('learning_logs:index')
        response = self.client.get(path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'learning_logs/index.html')


