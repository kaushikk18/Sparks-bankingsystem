from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home-page'),
    path('about-us', views.about_us, name='about-us'),
    path('all-customers', views.all_customers, name='all-customers'),
    # path('single-customer', views.single_customer, name='single-customer'),
    path("all-customers/<slug:slug>", views.singlecustomer,
         name="single-customer"),
    path("all-customers/<slug:slug>/transact",
         views.transact, name='transact-page'),
    path('reviews', views.review, name='review-page'),
    path("thank-you", views.thank_you),
    path('transaction-record', views.transaction_history, name='transaction-record')
]
