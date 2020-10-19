from django.db import models

# Create your models here.

#
from index.models import TBook
from user.models import TUser


class ShoppingCart(models.Model):
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    book_num = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'shopping_cart'