from django.contrib import admin
import review.models as rm

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'street_name', 'house_number', 'location', 'review', 'image', 'created', )


admin.site.register(rm.Review, ReviewAdmin)

