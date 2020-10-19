# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class OrderItem(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey('TBook', models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    order = models.ForeignKey('TOrder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item'


class ShoppingCart(models.Model):
    book = models.ForeignKey('TBook', models.DO_NOTHING, blank=True, null=True)
    book_num = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_cart'


class TAddress(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    detail_address = models.CharField(max_length=100, blank=True, null=True)
    cellphone = models.CharField(max_length=20, blank=True, null=True)
    post_code = models.CharField(max_length=6, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_address'


class TBook(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=50, blank=True, null=True)
    book_author = models.CharField(max_length=50, blank=True, null=True)
    book_pulish = models.CharField(max_length=50, blank=True, null=True)
    pulish_time = models.DateField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    book_isbn = models.CharField(max_length=20, blank=True, null=True)
    word_count = models.IntegerField(blank=True, null=True)
    open_type = models.CharField(max_length=20, blank=True, null=True)
    page_count = models.IntegerField(blank=True, null=True)
    class_field = models.ForeignKey('TClass', models.DO_NOTHING, db_column='class_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    book_wrapper = models.CharField(max_length=20, blank=True, null=True)
    book_paper = models.CharField(max_length=20, blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)
    editor_recommendatio = models.IntegerField(blank=True, null=True)
    content_introduction = models.CharField(max_length=20, blank=True, null=True)
    product_image_path = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book'


class TClass(models.Model):
    class_name = models.CharField(max_length=20, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_class'


class TOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField(blank=True, null=True)
    all_price = models.IntegerField(blank=True, null=True)
    address = models.ForeignKey(TAddress, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    create_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'


class TUser(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'
