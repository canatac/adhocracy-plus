# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-28 09:51
from __future__ import unicode_literals

from django.db import migrations


def rename_app(apps, schema_editor):
    Phase = apps.get_model("a4phases", "Phase")
    for phase in Phase.objects.all():
        phase.type = phase.type.replace(
            'meinberlin',
            'liqd_product')
        phase.save()


def backname_app(apps, schema_editor):
    Phase = apps.get_model("a4phases", "Phase")
    for phase in Phase.objects.all():
        phase.type = phase.type.replace(
            'liqd_product',
            'meinberlin')
        phase.save()


class Migration(migrations.Migration):

    replaces = [('liqd_product_ideas', '0017_rename_app_in_phase_type')]

    dependencies = [
        ('a4_candy_ideas', '0016_update_content_types'),
    ]

    operations = [
        migrations.RunPython(rename_app, backname_app)
    ]
