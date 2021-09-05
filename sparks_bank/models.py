from django.db import models

# Create your models here.


class customer(models.Model):
    cust_name = models.CharField(max_length=50)
    cust_id = models.IntegerField()
    cust_email = models.EmailField()
    current_balance = models.IntegerField()
    slug = models.SlugField(null=True)

    def __str__(self):
        return f"{self.cust_name} ({self.cust_id})"


class transaction_record(models.Model):

    transactor = models.CharField(max_length=50)
    revolver = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.transactor} ({self.amount})"


class testmodel(models.Model):
    test1 = models.CharField(max_length=50)
    test2 = models.CharField(max_length=50)


class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
