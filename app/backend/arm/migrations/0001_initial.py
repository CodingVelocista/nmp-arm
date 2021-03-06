# Generated by Django 2.2.5 on 2019-09-13 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationEquipmentOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationRiskRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicator_name', models.CharField(max_length=50)),
                ('risk_value', models.IntegerField()),
                ('risk_display_text', models.CharField(choices=[('Low', 'Low'), ('Low-Med', 'Low-Med'), ('Medium', 'Medium'), ('Med-High', 'Med-High'), ('High', 'High'), ('Extreme', 'Extreme')], default='Low', max_length=10)),
                ('caution_message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CautionMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_name', models.CharField(max_length=30)),
                ('risk_caution_value', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('message', models.TextField(default='add a message', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CriticalAreaRiskRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=10)),
                ('risk_value', models.IntegerField()),
                ('risk_display_text', models.CharField(choices=[('Low', 'Low'), ('Low-Med', 'Low-Med'), ('Medium', 'Medium'), ('Med-High', 'Med-High'), ('High', 'High'), ('Extreme', 'Extreme')], default='Low', max_length=10)),
                ('caution_message', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ForageDensityOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('description', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ForageHeightOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=1, max_digits=3)),
                ('description', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManureSetbackDistanceRiskRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_minimum', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('distance_maximum', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('risk_value', models.IntegerField()),
                ('risk_display_text', models.CharField(choices=[('Low', 'Low'), ('Low-Med', 'Low-Med'), ('Medium', 'Medium'), ('Med-High', 'Med-High'), ('High', 'High'), ('Extreme', 'Extreme')], default='Low', max_length=10)),
                ('caution_message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RestrictionStopMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_name', models.CharField(max_length=30)),
                ('stop_message', models.TextField(default='add a message', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RiskCutoffSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_level_name', models.CharField(max_length=4)),
                ('display', models.CharField(max_length=11)),
                ('minimum_score', models.IntegerField()),
                ('maximum_score', models.IntegerField()),
                ('message', models.TextField(default='add a message', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RiskRatingValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_name', models.CharField(max_length=30)),
                ('value_list', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SoilMoistureOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('description', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoilTypeOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoilTypeRiskRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soil_type', models.CharField(max_length=10)),
                ('risk_value', models.IntegerField()),
                ('risk_display_text', models.CharField(choices=[('Low', 'Low'), ('Low-Med', 'Low-Med'), ('Medium', 'Medium'), ('Med-High', 'Med-High'), ('High', 'High'), ('Extreme', 'Extreme')], default='Low', max_length=10)),
                ('caution_message', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurfaceConditionOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurfaceConditionRiskRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surface_condition', models.CharField(max_length=10)),
                ('is_a_stop_application_item', models.BooleanField(default=False)),
                ('risk_value', models.IntegerField()),
                ('risk_display_text', models.CharField(choices=[('Low', 'Low'), ('Low-Med', 'Low-Med'), ('Medium', 'Medium'), ('Med-High', 'Med-High'), ('High', 'High'), ('Extreme', 'Extreme')], default='Low', max_length=10)),
                ('caution_message', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterTableDepthOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]