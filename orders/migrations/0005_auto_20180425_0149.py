# Generated by Django 2.0.4 on 2018-04-25 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20180416_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='billing_address', to='addresses.Address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='billing_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='billing.BillingProfile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carts.Cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipping_address', to='addresses.Address'),
        ),
    ]
