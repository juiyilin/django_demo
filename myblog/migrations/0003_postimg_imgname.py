# Generated by Django 2.2.7 on 2020-02-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_postimg_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimg',
            name='imgname',
            field=models.CharField(default='', max_length=20),
        ),
    ]
