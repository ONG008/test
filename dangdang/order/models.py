from django.db import models

# Create your models here.
# from index.models import TAddress, TBook

# from user.models import TUser


#
from index.models import TBook
from user.models import TUser


class TAddress(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    detail_address = models.CharField(max_length=100, blank=True, null=True)
    cellphone = models.CharField(max_length=20, blank=True, null=True)
    post_code = models.CharField(max_length=6, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 't_address'


class TOrder(models.Model):
    # id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(blank=True, null=True)
    all_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    address = models.ForeignKey(TAddress, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING, blank=True, null=True)
    create_time = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 't_order'


class OrderItem(models.Model):
    # id = models.AutoField(primary_key=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'order_item'
