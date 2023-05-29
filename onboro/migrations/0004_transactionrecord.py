# Generated by Django 4.1.1 on 2023-05-27 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onboro', '0003_book_chapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.IntegerField(choices=[(1, 'チャージ'), (2, '使用')], verbose_name='種類')),
                ('amount', models.PositiveIntegerField(verbose_name='金額')),
                ('datetime', models.DateTimeField(verbose_name='日時')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='onboro.book', verbose_name='書籍')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name': '取引記録',
                'verbose_name_plural': '取引記録',
            },
        ),
    ]