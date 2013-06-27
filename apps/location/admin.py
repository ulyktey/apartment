from django.contrib import admin
from models import Region, City, District, Street
from forms import StreetForm

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name', )
    search_fields = ('name', )

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region_name', )
    list_display_links = ('name', )
    search_fields = ('name', )
    list_filter = ('region', )

    def region_name(self, instance):
        return instance.region.name

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_name', )
    list_display_links = ('name', )
    search_fields = ('name', )
    list_filter = ('city', )

    def city_name(self, instance):
        return instance.city.name

class StreetAdmin(admin.ModelAdmin):
    list_display = ('name', 'district_name', 'city_name', )
    list_display_links = ('name', )
    search_fields = ('name', )
    list_filter = ('district', )
    fields = ('district', 'name')
    form = StreetForm

    def district_name(self, instance):
        return instance.district.name

    def city_name(self, instance):
        return instance.district.city.name

admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Street, StreetAdmin)

