# Generated by Django 4.2.3 on 2023-07-31 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_blog_post_publish_bb7600_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
    ]
