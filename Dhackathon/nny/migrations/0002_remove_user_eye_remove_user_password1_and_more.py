# Generated by Django 4.0.3 on 2022-08-10 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nny', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='eye',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eye', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]