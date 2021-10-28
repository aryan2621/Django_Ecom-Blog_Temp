from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300, default="")
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=10, default='')
    phone = models.IntegerField(default=0)
    desc = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000, default='')
    name = models.CharField(max_length=90, default='')
    email = models.CharField(max_length=111, default='')
    amount = models.IntegerField(default=0)
    address = models.CharField(max_length=111, default='')
    city = models.CharField(max_length=111, default='')
    state = models.CharField(max_length=111, default='')
    zip = models.CharField(max_length=111, default='')
    phone = models.CharField(max_length=13, default=0)

    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
