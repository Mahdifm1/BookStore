# Generated by Django 4.2.4 on 2023-09-18 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
