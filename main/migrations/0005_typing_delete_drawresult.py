# Generated by Django 4.0.5 on 2023-07-04 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_drawresult_delete_lottodraws_delete_typing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Typing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('isplus', models.BooleanField()),
                ('draw', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='main.lottodraw')),
            ],
        ),
        migrations.DeleteModel(
            name='DrawResult',
        ),
    ]
