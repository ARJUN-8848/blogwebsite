# Generated by Django 5.1.1 on 2024-09-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0007_remove_blog_featured_image1_blog_content1'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='featured_image1',
            field=models.ImageField(blank=True, null=True, upload_to='featured_images'),
        ),
    ]