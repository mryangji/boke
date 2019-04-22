# Generated by Django 2.1.5 on 2019-02-28 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_replays_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField(default=0)),
                ('num', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.USER_upload')),
                ('userID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
    ]
