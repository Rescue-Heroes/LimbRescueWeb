# Generated by Django 3.2.4 on 2021-06-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limb', '0002_ppg_uploaded_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ppg',
            name='ppgdata',
            field=models.FileField(upload_to='ppgdatafile/<django.db.models.fields.CharField>'),
        ),
    ]
