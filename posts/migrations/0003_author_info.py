# Generated by Django 5.0 on 2024-04-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='info',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
