# Generated by Django 4.1.3 on 2022-12-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0019_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='profile2.png', null=True, upload_to='static/images/profile'),
        ),
    ]
