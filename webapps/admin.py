from django.contrib import admin
from webapps.models import *

admin.site.register(instrument_files)
admin.site.register(def_files)
admin.site.register(setting_files)
admin.site.register(signal_def_files)
admin.site.register(seq_defs)
admin.site.register(time_scales)
admin.site.register(date_formats)
admin.site.register(resolution)
admin.site.register(instruments)
admin.site.register(populations)


# Register your models here.
