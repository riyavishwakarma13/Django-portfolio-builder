# Generated by Django 3.2.7 on 2021-09-28 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_createportfolio_templates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createportfolio',
            name='brand_name',
        ),
        migrations.RemoveField(
            model_name='createportfolio',
            name='heading',
        ),
    ]
