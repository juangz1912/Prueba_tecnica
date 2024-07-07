# Generated by Django 4.1 on 2024-07-07 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='reservation',
            name='shift',
            field=models.CharField(choices=[('7-8', '7:00 AM - 8:00 AM'), ('8-9', '8:00 AM - 9:00 AM'), ('9-10', '9:00 AM - 10:00 AM'), ('10-11', '10:00 AM - 11:00 AM'), ('11-12', '11:00 AM - 12:00 PM'), ('13-14', '1:00 PM - 2:00 PM'), ('14-15', '2:00 PM - 3:00 PM'), ('15-16', '3:00 PM - 4:00 PM'), ('16-17', '4:00 PM - 5:00 PM'), ('17-18', '5:00 PM - 6:00 PM'), ('18-19', '6:00 PM - 7:00 PM'), ('19-20', '7:00 PM - 8:00 PM')], default='7-8', max_length=7),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('amenity', 'shift')},
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='start_time',
        ),
    ]
