# Generated by Django 4.2.4 on 2023-09-19 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='a@a.com', max_length=254),
        ),
    ]
