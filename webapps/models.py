from django.db import models

# This is the history data
class History_data_file(models.Model):
  name = models.CharField(max_length=30)
  path = models.CharField(max_length=200)

# Exchange rule file for the instrument
class Instrument_def_file(models.Model):
  name = models.CharField(max_length=30)
  path = models.CharField(max_length=200)

# Titan simulation settings
class Simulation_setting_file(models.Model):
  name = models.CharField(max_length=30)
  path = models.CharField(max_length=200)

# Signal settings, defines the argument range of the signals
class Signal_def_file(models.Model):
  name = models.CharField(max_length=30)
  path = models.CharField(max_length=200)

class Seq_def(models.Model):
  name = models.CharField(max_length=30)
  description = models.CharField(max_length=30)

class Time_scale(models.Model):
  name = models.CharField(max_length=30)

class Date_format(models.Model):
  name = models.CharField(max_length=10)
  format = models.CharField(max_length=30)

# Default resolutions
class Resolution(models.Model):
  value = models.CharField(max_length=10)

class Instrument(models.Model):
  name = models.CharField(max_length=30)
  history_data_file = models.ForeignKey(History_data_file, on_delete=models.CASCADE)
  instrument_def_file = models.ForeignKey(Instrument_def_file, on_delete=models.CASCADE)
  time_scale = models.ForeignKey(Time_scale, on_delete=models.CASCADE)
  date_format = models.ForeignKey(Date_format, on_delete=models.CASCADE)
  min_movement = models.CharField(max_length=30)
  price_scale = models.CharField(max_length=30)
  big_point_value = models.CharField(max_length=30)

class Population(models.Model):
  name = models.CharField(max_length=30)
  instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
  simulation_setting_file = models.ForeignKey(Simulation_setting_file, on_delete=models.CASCADE)
  signal_def_file = models.ForeignKey(Signal_def_file, on_delete=models.CASCADE)
  seq_def = models.ForeignKey(Seq_def, on_delete=models.CASCADE)
  start_date = models.CharField(max_length=30)
  end_date = models.CharField(max_length=30)
