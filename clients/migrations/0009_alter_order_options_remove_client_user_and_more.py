# Generated by Django 4.1.1 on 2022-09-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_alter_client_active_alter_client_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.AlterField(
            model_name='client',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='bottles_ordered',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='фотография'),
        ),
        migrations.AlterField(
            model_name='order',
            name='contacts',
            field=models.CharField(help_text='Введите Ваш номер телефона, адрес электронной почты или социальной сети', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, help_text='Вы можете добавить описание', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(help_text='Введите Ваше имя', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения заказа'),
        ),
    ]
