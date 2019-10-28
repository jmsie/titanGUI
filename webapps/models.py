from django.db import models

class Seq_def(models.Model):
  name = models.CharField(max_length=30)
  description = models.CharField(max_length=60)

# Default resolutions
class Resolution(models.Model):
  value = models.CharField(max_length=10)

class Instrument(models.Model):
  name = models.CharField(max_length=30)
  history_data_file = models.CharField(max_length=30)
  instrument_def_file = models.CharField(max_length=30)
  time_scale = models.CharField(max_length=5)
  date_format = models.CharField(max_length=10)
  min_movement = models.CharField(max_length=10)
  price_scale = models.CharField(max_length=10)
  big_point_value = models.CharField(max_length=10)
  query = models.CharField(max_length=200)
  start_date = models.DateField()
  end_date = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)



  def dump(self):
    print(self.name)
    print(self.history_data_file)
    print(self.instrument_def_file)
    print(self.time_scale)
    print(self.date_format)
    print(self.min_movement)
    print(self.price_scale)
    print(self.big_point_value)
    print(self.query)


class Population(models.Model):
  name = models.CharField(max_length=30)
  instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
  simulation_setting_file = models.CharField(max_length=30)
  signal_def_file = models.CharField(max_length=30)
  seq_def = models.ForeignKey(Seq_def, on_delete=models.CASCADE)
  start_date = models.CharField(max_length=30)
  end_date = models.CharField(max_length=30)
  resolutions = models.CharField(max_length=60)
  query = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
