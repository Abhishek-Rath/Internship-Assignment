# Generated by Django 4.0.4 on 2022-05-01 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddConstraint(
            model_name='item',
            constraint=models.CheckConstraint(check=models.Q(('price__gte', 1)), name='Price >= 1'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='bills.item'),
        ),
        migrations.AddConstraint(
            model_name='invoice',
            constraint=models.CheckConstraint(check=models.Q(('quantity__gte', 1)), name='Quantity >= 1'),
        ),
    ]
