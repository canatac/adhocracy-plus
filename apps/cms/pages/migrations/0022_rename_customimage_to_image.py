# Generated by Django 2.2.4 on 2019-08-22 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_cms_pages', '0021_remove_homepage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='custom_image',
            new_name='image',
        ),
    ]