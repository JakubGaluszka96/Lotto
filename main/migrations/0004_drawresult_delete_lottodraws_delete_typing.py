# Generated by Django 4.0.5 on 2023-07-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_typing_betlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrawResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='LottoDraws',
        ),
        migrations.DeleteModel(
            name='Typing',
        ),
    ]