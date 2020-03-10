# Generated by Django 3.0.4 on 2020-03-10 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drive_data', '0002_auto_20200310_1644'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='drive',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drive_user', to='drive_data.Folder'),
        ),
    ]
