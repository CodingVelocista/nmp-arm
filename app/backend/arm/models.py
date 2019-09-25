from django.db import models

RATING_DISPLAY_TEXT = (
    ('Low', 'Low'),
    ('Low-Med', 'Low-Med'),
    ('Medium', 'Medium'),
    ('Med-High', 'Med-High'),
    ('High', 'High'),
    ('Extreme', 'Extreme'),
)

class FormField(models.Model):
    
    field_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, default='', blank=True, null=True)

    def __str__(self):
        return "{0}: {1}".format(self.field_name, self.description)


class ForageHeightOption(models.Model):

    value = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "value:{0}, description:{1}, active:{2}".format(self.value, self.description, self.active)

class WaterTableDepthOption(models.Model):

    value = models.IntegerField()
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

class SoilTypeOption(models.Model):

    value = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

class SoilMoistureOption(models.Model):

    value = models.IntegerField()
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

class ForageDensityOption(models.Model):

    value = models.IntegerField()
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

class SurfaceConditionOption(models.Model):

    value = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    
class ApplicationEquipmentOption(models.Model):

    value = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

class RestrictionStopMessage(models.Model):

    risk_name = models.CharField(max_length=30)
    stop_message = models.TextField(max_length=500, default='add a message', blank=False, null=False)

class RiskCutoffSetting(models.Model):

    risk_level_name = models.CharField(max_length=4)
    display = models.CharField(max_length=11)
    minimum_score = models.IntegerField()
    maximum_score = models.IntegerField()
    message = models.TextField(max_length=500, default='add a message', blank=False, null=False)


class NumericRiskRatingMixin(models.Model):
    class Meta:
        abstract=True

    range_minimum = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    range_maximum = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    risk_value = models.IntegerField(blank=False, null=False)
    risk_display_text = models.CharField(max_length=10, default='Low', choices=RATING_DISPLAY_TEXT)
    caution_message = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return "range_minimum:{0}, range_maximum:{1}, risk_value:{2}, risk_display_text:{3}, caution_message:{4}".format(self.range_minimum, self.range_maximum, self.risk_value, self.risk_display_text, self.caution_message)

class Preciptation24RiskRating(NumericRiskRatingMixin):
    pass

class Preciptation72RiskRating(NumericRiskRatingMixin):
    pass

class SoilMoistureRiskRating(NumericRiskRatingMixin):
    pass

class WaterTableRiskRating(NumericRiskRatingMixin):
    pass

class ForageDensityRiskRating(NumericRiskRatingMixin):
    pass

class ForageHeightRiskRating(NumericRiskRatingMixin):
    pass

class ApplicationRiskRating(models.Model):

    applicator_name = models.CharField(max_length=50, blank=False, null=False)
    risk_value = models.IntegerField(blank=False, null=False)
    risk_display_text = models.CharField(max_length=10, default='Low', choices=RATING_DISPLAY_TEXT)
    caution_message = models.TextField(max_length=500, blank=False, null=False)

class SoilTypeRiskRating(models.Model):

    soil_type = models.CharField(max_length=10, blank=False, null=False)
    risk_value = models.IntegerField(blank=False, null=False)
    risk_display_text = models.CharField(max_length=10, default='Low', choices=RATING_DISPLAY_TEXT)
    caution_message = models.TextField(max_length=500, blank=True, null=True)

class SurfaceConditionRiskRating(models.Model):

    surface_condition = models.CharField(max_length=10, blank=False, null=False)
    is_a_stop_application_item = models.BooleanField(default=False)
    risk_value = models.IntegerField(blank=False, null=False)
    risk_display_text = models.CharField(max_length=10, default='Low', choices=RATING_DISPLAY_TEXT)
    caution_message = models.TextField(max_length=500, blank=True, null=True)

class CriticalAreaRiskRating(models.Model):

    answer = models.CharField(max_length=10, blank=False, null=False)
    risk_value = models.IntegerField(blank=False, null=False)
    risk_display_text = models.CharField(max_length=10, default='Low', choices=RATING_DISPLAY_TEXT)
    caution_message = models.TextField(max_length=500, blank=True, null=True)

class ManureSetbackDistanceRiskRating(models.Model):

    distance_minimum = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0)
    distance_maximum = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0)
    risk_value = models.IntegerField(blank=False, null=False)
    risk_display_text = models.CharField(max_length=10, default='Low', choices=RATING_DISPLAY_TEXT)
    caution_message = models.TextField(max_length=500, blank=False, null=False)