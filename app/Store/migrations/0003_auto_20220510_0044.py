# Generated by Django 3.2.13 on 2022-05-10 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_rename_name_ebook_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ebook',
            name='img_url',
        ),
        migrations.AddField(
            model_name='ebook',
            name='img_static',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]