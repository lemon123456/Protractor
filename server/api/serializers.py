# -*- coding: utf-8 -*-

from rest_framework import serializers
from server.models import Provider, OperationSystem, HardDisk, Instance


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'


class SystemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OperationSystem
        fields = '__all__'


class HardDiskSerializer(serializers.ModelSerializer):

    class Meta:
        model = HardDisk
        fields = '__all__'


class InstanceSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer()
    system = SystemSerializer()
    hd = HardDiskSerializer()

    class Meta:
        model = Instance
        fields = '__all__'
