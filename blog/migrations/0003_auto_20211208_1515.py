# Generated by Django 3.2.9 on 2021-12-08 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tags_id',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
