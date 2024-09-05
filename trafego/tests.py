#--------------------# CREATE THE UNIT TESTS #--------------------#
#10 TESTS TOTAL

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import SegEstrada
from django.contrib.auth.models import User

#Class that contains the unit tests
class SegEstradaAPITests(APITestCase):
    def setUp(self):
        #dummy instances
        SegEstrada.objects.create(id=1, long_start=0.0, lat_start=0.0, long_end=1.0, lat_end=1.0, length=10.0, speed=60.0)
        SegEstrada.objects.create(id=2, long_start=1.0, lat_start=1.0, long_end=2.0, lat_end=2.0, length=20.0, speed=35.0)
        SegEstrada.objects.create(id=3, long_start=2.0, lat_start=2.0, long_end=3.0, lat_end=3.0, length=30.0, speed=15.0)

        #Admin user test
        self.Admin_user = User.objects.create_superuser(username='Admin', password='password_admin')

    #The tests are made to use different actions from admin and anon and check if it's valid or forbidden - permissions testa

    #CREATE SEGMENTS: ADMIN VS ANON

    def test_create_segment_as_Admin(self):
        self.client.login(username='Admin', password='password_admin')
        url = reverse('segestrada-list')
        data = {
            "id": 4,
            "long_start": 3.0,
            "lat_start": 3.0,
            "long_end": 4.0,
            "lat_end": 4.0,
            "length": 40.0,
            "speed": 25.0,
            "tempo_reg": "2024-09-04T12:00:00Z"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SegEstrada.objects.count(), 4)
        self.assertEqual(SegEstrada.objects.get(id=4).speed, 25.0)

    def test_create_segment_as_Anon(self):
        url = reverse('segestrada-list')
        data = {
            "id": 4,
            "long_start": 3.0,
            "lat_start": 3.0,
            "long_end": 4.0,
            "lat_end": 4.0,
            "length": 40.0,
            "speed": 25.0,
            "tempo_reg": "2024-09-04T12:00:00Z"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    #UPDATE SEGMENTS: ADMIN VS ANON

    def test_update_segment_as_Admin(self):
        self.client.login(username='Admin', password='password_admin')
        url = reverse('segestrada-detail', args=[1])
        data = {
            "speed": 55.0
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SegEstrada.objects.get(id=1).speed, 55.0)

    def test_update_segment_as_Anon(self):
        url = reverse('segestrada-detail', args=[1])
        data = {
            "speed": 55.0
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    #DELETE SEGMENTS: ADMIN VS ANON

    def test_delete_segment_as_Admin(self):
        self.client.login(username='Admin', password='password_admin')
        url = reverse('segestrada-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SegEstrada.objects.count(), 2)

    def test_delete_segment_as_Anon(self):
        url = reverse('segestrada-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(SegEstrada.objects.count(), 3)

    #FILTERING SEGMENTS: TEST ALL THE ALTERNATIVES INTRODUCED

    def test_filter_by_intensity_low(self):
        url = reverse('segestrada-list') + '?intensity=low'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 1)

    def test_filter_by_intensity_medium(self):
        url = reverse('segestrada-list') + '?intensity=medium'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 2)

    def test_filter_by_intensity_high(self):
        url = reverse('segestrada-list') + '?intensity=high'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 3)

    def test_filter_by_intensity_alternative_terms(self):
        # Testing alternative terms for "low"
        url = reverse('segestrada-list') + '?intensity=l'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 1)

        url = reverse('segestrada-list') + '?intensity=baixa'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 1)

        # Testing alternative terms for "medium"
        url = reverse('segestrada-list') + '?intensity=m'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 2)

        url = reverse('segestrada-list') + '?intensity=media'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 2)

        # Testing alternative terms for "high"
        url = reverse('segestrada-list') + '?intensity=h'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 3)

        url = reverse('segestrada-list') + '?intensity=elevada'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 3)

