# Generated by Django 2.1.5 on 2019-02-22 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('userAccount', models.CharField(max_length=30, unique=True)),
                ('userPassword', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('userNickname', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('userQQ', models.CharField(max_length=30)),
                ('userSign', models.CharField(max_length=200)),
                ('userPicture', models.CharField(max_length=200)),
                ('userID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
    ]
