# Generated by Django 3.2.7 on 2021-09-27 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210927_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createportfolio',
            name='id',
        ),
        migrations.AddField(
            model_name='createportfolio',
            name='template_url',
            field=models.SlugField(default=1, max_length=200, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
