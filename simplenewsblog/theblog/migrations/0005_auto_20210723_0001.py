# Generated by Django 3.2.5 on 2021-07-23 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='IT', max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
