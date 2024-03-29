# Generated by Django 4.0.5 on 2023-07-18 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_betlist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='typeslist',
        ),
        migrations.AddField(
            model_name='bet',
            name='name',
            field=models.CharField(max_length=1000, null='bet'),
            preserve_default='bet',
        ),
        migrations.AddField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='BetList',
        ),
    ]
