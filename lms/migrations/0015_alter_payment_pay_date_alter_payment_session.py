# Generated by Django 5.0.1 on 2024-01-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0014_remove_payment_payment_summ_course_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pay_date',
            field=models.DateField(auto_now_add=True, verbose_name='дата оплаты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='session',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='cессия для оплаты'),
        ),
    ]