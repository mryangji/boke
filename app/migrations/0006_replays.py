# Generated by Django 2.1.5 on 2019-02-22 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_user_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replays',
            fields=[
                ('replay_num', models.AutoField(primary_key=True, serialize=False)),
                ('replay', models.CharField(max_length=1000)),
                ('num', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.USER_upload')),
            ],
        ),
    ]