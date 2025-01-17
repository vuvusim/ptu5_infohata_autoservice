# Generated by Django 4.1.3 on 2022-11-14 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0002_alter_carmodel_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='estimate_date',
            field=models.DateField(blank=True, null=True, verbose_name='estimate_date'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('n', 'new'), ('a', 'advanced payment'), ('o', 'ordered parts'), ('w', 'working'), ('p', 'paid'), ('c', 'canceled'), ('d', 'done')], default='n', max_length=1, verbose_name='status'),
        ),
    ]
