# Generated by Django 4.2.7 on 2023-12-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joylist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='joy',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='joy',
            name='compelete',
        ),
        migrations.AlterField(
            model_name='joy',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Details'),
        ),
        migrations.AlterField(
            model_name='joy',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Big idea'),
        ),
    ]
