# Generated by Django 3.2.9 on 2021-12-08 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
    ]