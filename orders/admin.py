from django.contrib import admin

from orders.models import Order, OrderItem

class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "quantity"
    search_fields = (
        "product",
        "name",
    )
    extra = 0

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "name", "price", "quantity"
    search_fields = (
        "order",
        "product",
        "name",
    )
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp"
    )
    
    search_fields = (
        "id",
        "requires_delivery",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    
    readonly_fields = (
        "created_timestamp",
    )
    
    list_filter = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    
    inlines = (OrderItemTabulareAdmin,)

   
class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",  
    )
    
    search_fields = (
        "requires_delivery",
        "payment_on_get",
        "is_paid",
        "created_timestamp"
    )
    
    readonly_fields = ("created_timestamp",)
    extra = 0
    
