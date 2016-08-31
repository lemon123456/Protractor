# -*- coding: utf-8 -*-

from django.conf.urls import url
from views import ProviderView, SystemView, HardDiskView, InstanceView

urlpatterns = [
    url(r'^provider/list', ProviderView.as_view(), name='provider_list'),
    url(r'^system/list', SystemView.as_view(), name='system_list'),
    url(r'^hd/list', HardDiskView.as_view(), name='hd_list'),
    url(r'^instance/list', InstanceView.as_view(), name='instance_list')
]
