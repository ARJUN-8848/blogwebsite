# Generated by Django 5.1.1 on 2024-09-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0013_alter_blog_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='heading1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]