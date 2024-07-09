from django.db import models

class CreateMap(models.Model):
    map_name = models.CharField(max_length=100)
    map_groups = models.TextField(max_length=99999, null=True, blank=True)
    map_hosts = models.TextField(max_length=99999, null=True, blank=True)
    map_ips = models.TextField(max_length=99999, null=True, blank=True)
    map_hosts_filter = models.TextField(max_length=99999, null=True, blank=True)
    create_link = models.BooleanField(default=False)
    add_trigger = models.BooleanField(default=False)
    unavailable_by_icmp = models.BooleanField(default=False)
    snmp_not_responding = models.BooleanField(default=False)
