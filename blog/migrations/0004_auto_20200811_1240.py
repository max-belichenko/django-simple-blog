# Generated by Django 3.0.6 on 2020-08-11 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200811_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('publish', 'Can publish post.')]},
        ),
    ]