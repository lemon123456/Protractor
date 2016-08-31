# -*- coding: utf-8 -*-
import json

from django.test import TestCase

from rest_framework.test import APITestCase
from models import Provider, OperationSystem, Instance, HardDisk

# Create your tests here.


class ServerTestCase(TestCase):

    def setUp(self):
        """start test object"""
        Provider.objects.create(name='Amazon')
        OperationSystem.objects.create(name='Windows')
        HardDisk.objects.create(hd_type='ssd', amount_of_hd=40.0)

    def teste_get_object(self):

        provider = Provider.objects.get(name='Amazon')
        system = OperationSystem.objects.get(name='Windows')
        hd = HardDisk.objects.get(hd_type='ssd')
        self.assertEqual(provider.name, 'Amazon')
        self.assertEqual(system.name, 'Windows')
        self.assertEqual(hd.__str__(), '40.0 ssd')

    def test_add_instance_object(self):

        provider = Provider.objects.get(name='Amazon')
        system = OperationSystem.objects.get(name='Windows')
        hd = HardDisk.objects.get(hd_type='ssd')
        Instance.objects.create(name='Instance1',
                                amount_of_cpu=2,
                                amount_of_memory=256,
                                provider=provider,
                                hd=hd,
                                price=49.00,
                                system=system)
        instance = Instance.objects.filter(provider=provider,
                                           system=system)
        self.assertEqual(len(instance), 1)
        self.assertEqual(len(instance.filter(price__gte=40)), 1)


class ServerApiTestCase(APITestCase):

    def setUp(self):
        """start test object"""
        Provider.objects.create(name='Amazon')
        OperationSystem.objects.create(name='Windows')
        HardDisk.objects.create(hd_type='ssd', amount_of_hd=40.0)
        provider = Provider.objects.get(name='Amazon')
        system = OperationSystem.objects.get(name='Windows')
        hd = HardDisk.objects.get(hd_type='ssd')
        Instance.objects.create(name='Instance1',
                                amount_of_cpu=2,
                                amount_of_memory=256,
                                provider=provider,
                                hd=hd,
                                price=49.00,
                                system=system)

    def test_get_provider(self):
        request = self.client.get('/api/provider/list/')
        self.assertEqual(request.status_code, 200)

    def test_get_system(self):
        request = self.client.get('/api/system/list/')
        self.assertEqual(request.status_code, 200)

    def test_get_hd(self):
        request = self.client.get('/api/hd/list/')
        self.assertEqual(request.status_code, 200)

    def test_get_instnce(self):
        Provider.objects.create(name='Digital Ocean')
        OperationSystem.objects.create(name='Ubuntu')
        HardDisk.objects.create(hd_type='hdd', amount_of_hd=100.0)
        provider = Provider.objects.get(name='Digital Ocean')
        system = OperationSystem.objects.get(name='Ubuntu')
        hd = HardDisk.objects.get(hd_type='hdd')
        Instance.objects.create(name='Instance test',
                                amount_of_cpu=5,
                                amount_of_memory=16,
                                provider=provider,
                                hd=hd,
                                price=180.00,
                                system=system)
        request = self.client.get('/api/instance/list/')
        self.assertEqual(request.status_code, 200)
        response = json.loads(request.content)
        self.assertEqual(type(response), list)
        request = self.client.get('/api/instance/list/?system=1')
        response = json.loads(request.content)
        self.assertEqual(len(response), 1)
        request = self.client.get('/api/instance/list/?amount_of_cpu=5')
        response = json.loads(request.content)
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]['price'], '180.00')


class ServerViewTest(TestCase):

    def test_return_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
