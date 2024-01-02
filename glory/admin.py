from django.contrib import admin
from .models import Ingredients, Juice, Room
# Register your models here.


class IngredientsInLine(admin.StackedInline):
    model = Ingredients
    extra = 1

class JuiceAdmin(admin.ModelAdmin):
    inlines = [IngredientsInLine]

admin.site.register(Juice, JuiceAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'room_number',
        'order_check'
    )

admin.site.register(Room, RoomAdmin)