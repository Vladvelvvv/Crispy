from django.contrib import admin

from carts.models import Cart

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "product", "quantity", "created_timestamp"
    search_fields = "product", "quantity", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user_name", "product_name", "quantity", "created_timestamp"]
    list_filter = ['created_timestamp', 'user', 'product__name']
    
    def user_name(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"
    
    def product_name(self, obj):
        return str(obj.product.name)