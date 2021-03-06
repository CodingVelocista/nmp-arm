# Generated by Django 2.2.5 on 2019-09-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arm', '0002_auto_20190924_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForageDensityRiskRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_value', models.IntegerField()),
                ('risk_display_text', models.CharField(choices=[('Low', 'Low'), ('Low-Med', 'Low-Med'), ('Medium', 'Medium'), ('Med-High', 'Med-High'), ('High', 'High'), ('Extreme', 'Extreme')], default='Low', max_length=10)),
                ('caution_message', models.TextField(blank=True, max_length=500, null=True)),
                ('show_stop_application', models.BooleanField(default=False)),
                ('stop_application_message', models.TextField(blank=True, max_length=500, null=True)),
                ('range_minimum', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('range_maximum', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ForageHeightRiskRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_value', models.IntegerField()),
                ('risk_display_text', models.CharField(choices=[('Low', 'Low'), ('Low-Med', 'Low-Med'), ('Medium', 'Medium'), ('Med-High', 'Med-High'), ('High', 'High'), ('Extreme', 'Extreme')], default='Low', max_length=10)),
                ('caution_message', models.TextField(blank=True, max_length=500, null=True)),
                ('show_stop_application', models.BooleanField(default=False)),
                ('stop_application_message', models.TextField(blank=True, max_length=500, null=True)),
                ('range_minimum', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('range_maximum', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Preciptation24RiskRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_value', models.IntegerField()),
                ('risk_display_text', models.CharField(choices=[('Low', 'Low'), ('Low-Med', 'Low-Med'), ('Medium', 'Medium'), ('Med-High', 'Med-High'), ('High', 'High'), ('Extreme', 'Extreme')], default='Low', max_length=10)),
                ('caution_message', models.TextField(blank=True, max_length=500, null=True)),
                ('show_stop_application', models.BooleanField(default=False)),
                ('stop_application_message', models.TextField(blank=True, max_length=500, null=True)),
                ('range_minimum', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('range_maximum', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Preciptation72RiskRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_value', models.IntegerField()),
                ('risk_display_text', models.CharField(choices=[('Low', 'Low'), ('Low-Med', 'Low-Med'), ('Medium', 'Medium'), ('Med-High', 'Med-High'), ('High', 'High'), ('Extreme', 'Extreme')], default='Low', max_length=10)),
                ('caution_message', models.TextField(blank=True, max_length=500, null=True)),
                ('show_stop_application', models.BooleanField(default=False)),
                ('stop_application_message', models.TextField(blank=True, max_length=500, null=True)),
                ('range_minimum', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('range_maximum', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SoilMoistureRiskRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_value', models.IntegerField()),
                ('risk_display_text', models.CharField(choices=[('Low', 'Low'), ('Low-Med', 'Low-Med'), ('Medium', 'Medium'), ('Med-High', 'Med-High'), ('High', 'High'), ('Extreme', 'Extreme')], default='Low', max_length=10)),
                ('caution_message', models.TextField(blank=True, max_length=500, null=True)),
                ('show_stop_application', models.BooleanField(default=False)),
                ('stop_application_message', models.TextField(blank=True, max_length=500, null=True)),
                ('range_minimum', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('range_maximum', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WaterTableRiskRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_value', models.IntegerField()),
                ('risk_display_text', models.CharField(choices=[('Low', 'Low'), ('Low-Med', 'Low-Med'), ('Medium', 'Medium'), ('Med-High', 'Med-High'), ('High', 'High'), ('Extreme', 'Extreme')], default='Low', max_length=10)),
                ('caution_message', models.TextField(blank=True, max_length=500, null=True)),
                ('show_stop_application', models.BooleanField(default=False)),
                ('stop_application_message', models.TextField(blank=True, max_length=500, null=True)),
                ('range_minimum', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('range_maximum', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='RestrictionStopMessage',
        ),
        migrations.RemoveField(
            model_name='surfaceconditionriskrating',
            name='is_a_stop_application_item',
        ),
        migrations.AddField(
            model_name='applicationriskrating',
            name='show_stop_application',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applicationriskrating',
            name='stop_application_message',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='criticalareariskrating',
            name='show_stop_application',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='criticalareariskrating',
            name='stop_application_message',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='manuresetbackdistanceriskrating',
            name='show_stop_application',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='manuresetbackdistanceriskrating',
            name='stop_application_message',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='soiltyperiskrating',
            name='show_stop_application',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='soiltyperiskrating',
            name='stop_application_message',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='surfaceconditionriskrating',
            name='show_stop_application',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='surfaceconditionriskrating',
            name='stop_application_message',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='applicationriskrating',
            name='caution_message',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='manuresetbackdistanceriskrating',
            name='caution_message',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
