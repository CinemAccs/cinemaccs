# Generated by Django 4.1.4 on 2022-12-10 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemaccs_project', '0002_remove_theater_zipcode_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theater',
            old_name='insertDate',
            new_name='createDate',
        ),
        migrations.AddField(
            model_name='theater',
            name='modifyDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='theater',
            name='zipcode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='theater',
            name='accessibilityDescription',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='theater',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
