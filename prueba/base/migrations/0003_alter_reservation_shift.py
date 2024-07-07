# Generated by Django 4.1 on 2024-07-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_reservation_unique_together_reservation_shift_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='shift',
            field=models.CharField(choices=[('07:00-08:00', '07:00-08:00'), ('08:00-09:00', '08:00-09:00'), ('09:00-10:00', '09:00-10:00'), ('10:00-11:00', '10:00-11:00'), ('11:00-12:00', '11:00-12:00'), ('13:00-14:00', '13:00-14:00'), ('14:00-15:00', '14:00-15:00'), ('15:00-16:00', '15:00-16:00'), ('16:00-17:00', '16:00-17:00'), ('17:00-18:00', '17:00-18:00'), ('18:00-19:00', '18:00-19:00'), ('19:00-20:00', '19:00-20:00')], max_length=20),
        ),
    ]
