# Generated by Django 2.2.3 on 2019-07-24 11:22

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('a4_candy_cms_settings', '0003_rename_table_to_default'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganisationSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', wagtail.core.fields.RichTextField()),
                ('contacts', wagtail.core.fields.RichTextField()),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]