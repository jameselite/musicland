# Generated by Django 5.1.1 on 2024-09-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0011_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=400),
        ),
    ]
