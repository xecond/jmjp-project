# Generated by Django 5.0.1 on 2024-02-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_corpinfo_delete_companyinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top500',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_field', models.IntegerField(blank=True, db_column='No.', null=True)),
                ('종목명', models.TextField(blank=True, null=True)),
                ('기준', models.IntegerField(blank=True, null=True)),
                ('시장', models.TextField(blank=True, null=True)),
                ('자산총계', models.IntegerField(blank=True, null=True)),
                ('자본금', models.IntegerField(blank=True, null=True)),
                ('자본총계', models.IntegerField(blank=True, null=True)),
                ('매출액', models.IntegerField(blank=True, null=True)),
                ('영업이익', models.IntegerField(blank=True, null=True)),
                ('순이익', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'top500',
                'managed': False,
            },
        ),
    ]
