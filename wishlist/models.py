from django.db import models
from django.conf import settings
from store.models import Product, Variation


class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name
    
    @property
    def name(self):
        return self.user.username


        #return f" {self.user} - {self.product_name}"