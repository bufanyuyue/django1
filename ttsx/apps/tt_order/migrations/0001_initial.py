# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(verbose_name='添加时间', auto_now=True)),
                ('update_date', models.DateTimeField(verbose_name='修改时间', auto_now_add=True)),
                ('isDelete', models.BooleanField(verbose_name='逻辑删除', default=False)),
                ('count', models.IntegerField(verbose_name='数量', default=1)),
                ('price', models.DecimalField(verbose_name='单价', decimal_places=2, max_digits=10)),
                ('comment', models.TextField(verbose_name='评价信息', default='')),
            ],
            options={
                'db_table': 'df_order_goods',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('add_date', models.DateTimeField(verbose_name='添加时间', auto_now=True)),
                ('update_date', models.DateTimeField(verbose_name='修改时间', auto_now_add=True)),
                ('isDelete', models.BooleanField(verbose_name='逻辑删除', default=False)),
                ('order_id', models.CharField(verbose_name='订单号', primary_key=True, serialize=False, max_length=64)),
                ('total_count', models.IntegerField(verbose_name='商品总数', default=1)),
                ('total_amount', models.DecimalField(verbose_name='商品总金额', decimal_places=2, max_digits=10)),
                ('trans_cost', models.DecimalField(verbose_name='运费', decimal_places=2, max_digits=10)),
                ('pay_method', models.SmallIntegerField(verbose_name='支付方式', choices=[(1, '货到付款'), (2, '支付宝')], default=1)),
                ('status', models.SmallIntegerField(verbose_name='订单状态', choices=[(1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成')], default=1)),
                ('trade_id', models.CharField(verbose_name='支付编号', unique=True, max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'df_order_info',
            },
        ),
    ]
