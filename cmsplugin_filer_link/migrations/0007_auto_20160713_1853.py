# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_link', '0006_auto_20160705_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerlinkplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=models.CASCADE,parent_link=True, related_name='cmsplugin_filer_link_filerlinkplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
