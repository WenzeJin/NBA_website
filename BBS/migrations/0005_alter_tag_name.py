# Generated by Django 5.0.6 on 2024-05-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBS', '0004_post_abstract_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
