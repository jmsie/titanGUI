from django.db import models

class Seq_def(models.Model):
  name = models.CharField(max_length=30, primary_key=True)
  description = models.CharField(max_length=60)

class Time_scale(models.Model):
  name = models.CharField(max_length=30, primary_key=True)

class Date_format(models.Model):
  name = models.CharField(max_length=10, primary_key=True)
  format = models.CharField(max_length=30)

# Default resolutions
class Resolution(models.Model):
  value = models.CharField(max_length=10, primary_key=True)

class Instrument(models.Model):
  name = models.CharField(max_length=30, primary_key=True)
  history_data_file = models.CharField(max_length=30)
  instrument_def_file = models.CharField(max_length=30)
  time_scale = models.ForeignKey(Time_scale, on_delete=models.CASCADE) # TODO change to ENUM
  date_format = models.ForeignKey(Date_format, on_delete=models.CASCADE) # TODO change to ENUM
  min_movement = models.CharField(max_length=30)
  price_scale = models.CharField(max_length=30)
  big_point_value = models.CharField(max_length=30)
  query = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)

class Population(models.Model):
  name = models.CharField(max_length=30, primary_key=True)
  instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
  simulation_setting_file = models.CharField(max_length=30)
  signal_def_file = models.CharField(max_length=30)
  seq_def = models.ForeignKey(Seq_def, on_delete=models.CASCADE)
  start_date = models.CharField(max_length=30)
  end_date = models.CharField(max_length=30)
  resolutions = models.CharField(max_length=60)
  query = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
