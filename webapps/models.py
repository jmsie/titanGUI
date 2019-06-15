from django.db import models

# This is the history data
class instrument_files(models.Model):
  name = models.CharField(max_length=30)
  path = models.CharField(max_length=200)

# Exchange rule file
class def_files(models.Model):
  name = models.CharField(max_length=30)
  path = models.CharField(max_length=200)

# Titan settings
class setting_files(models.Model):
  name = models.CharField(max_length=30)
  path = models.CharField(max_length=200)

# Signal settings, defines the argument range of the signals
class signal_def_files(models.Model):
  name = models.CharField(max_length=30)
  path = models.CharField(max_length=200)

class seq_defs(models.Model):
  name = models.CharField(max_length=30)

class time_scales(models.Model):
  name = models.CharField(max_length=30)

class date_formats(models.Model):
  name = models.CharField(max_length=10)
  format = models.CharField(max_length=30)

# Default resolutions
class resolution(models.Model):
  value = models.CharField(max_length=10)

class instruments(models.Model):
  name = models.CharField(max_length=30)
  instrument_file = models.ForeignKey(instrument_files, on_delete=models.CASCADE)
  def_file = models.ForeignKey(def_files, on_delete=models.CASCADE)
  time_scale = models.CharField(max_length=30)
  date_format = models.CharField(max_length=30)
  min_movement = models.CharField(max_length=30)
  price_scale = models.CharField(max_length=30)
  big_point_value = models.CharField(max_length=30)

class populations(models.Model):
  name = models.CharField(max_length=30)
  start_date = models.CharField(max_length=30)
  end_date = models.CharField(max_length=30)
  instrument = models.ForeignKey(instruments, on_delete=models.CASCADE)
  setting_file = models.ForeignKey(setting_files, on_delete=models.CASCADE)
  seq_def = models.CharField(max_length=30)
  signal_def = models.ForeignKey(signal_def_files, on_delete=models.CASCADE)


