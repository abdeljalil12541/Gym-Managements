# Generated by Django 3.2 on 2021-09-04 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_alter_trainermsg_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainermsg',
            name='user_type',
        ),
    ]