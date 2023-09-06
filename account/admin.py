from django.contrib import admin
from .models import Profile, Cart


class CartInline(admin.TabularInline):
    model = Cart
    extra = 0


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'wallet', 'is_active')
    fields = ('username', 'name', 'email', 'phone_number', 'wallet', 'is_active', 'date_joined')
    inlines = [CartInline]
    readonly_fields = ('date_joined',)
