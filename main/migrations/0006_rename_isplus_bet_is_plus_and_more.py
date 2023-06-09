# Generated by Django 4.0.5 on 2023-07-09 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_typing_delete_drawresult'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bet',
            old_name='isplus',
            new_name='is_plus',
        ),
        migrations.RenameField(
            model_name='typing',
            old_name='isplus',
            new_name='is_plus',
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('win', models.BooleanField()),
                ('bet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bet')),
            ],
        ),
    ]
