# Generated by Django 4.0.4 on 2022-05-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0003_alter_campmodel_description_alter_campmodel_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campmodel',
            name='description',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='campmodel',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='camps/'),
        ),
    ]
