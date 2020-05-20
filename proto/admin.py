from django.contrib.gis import admin

# from proto.models import Photo, Location, PhotographerSubscription
from proto.models import Photo, PhotographerSubscription
from proto.models import Photographer, Category

admin.site.register(Photographer)
admin.site.register(Photo)
admin.site.register(PhotographerSubscription)
# admin.site.register(Location)
admin.site.register(Category)
