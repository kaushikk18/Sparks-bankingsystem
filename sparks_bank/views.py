from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .forms import transactForm, ReviewForm

from .models import Review, customer, transaction_record
# Create your views here.


def index(request):
    return render(request, 'sparks_bank/index.html')


def about_us(request):
    return render(request, 'sparks_bank/aboutus.html')


def all_customers(request):
    customers = customer.objects.all()
    return render(request, 'sparks_bank/all-customers.html', {
        'customers': customers
    })


def single_customer(request, slug):

    if request.method == 'POST':
        return HttpResponseRedirect("/thank-you")

    else:
        single_customer = get_object_or_404(customer, slug=slug)
        # single_customer = customer.objects.get()
        form = transactForm()
        return render(request, 'sparks_bank/single-customer.html', {
            'name': single_customer.cust_name,
            'id': single_customer.cust_id,
            'form': form
        })


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = Review(
                user_name=form.cleaned_data['user_name'],
                review_text=form.cleaned_data['review_text'],
                rating=form.cleaned_data['rating'])
            review.save()
            return HttpResponseRedirect("/thank_you")

    else:
        form = ReviewForm()

    return render(request, "sparks_bank/single-customer.html", {
        "form": form
    })


'''''
def single_customer(request, slug):
    if request.method == 'POST':
        form = transactForm(request.POST)
        transactor_object = get_object_or_404(customer, slug=slug)
        revolver_object = get_object_or_404(
            customer, cust_name=form.cleaned_data['revolver'])
        amount = form.cleaned_data['amount']

        if form.is_valid():
            transactor_object.current_balance = transactor_object.current_balance - amount
            revolver_object.current_balance = revolver_object.current_balance + amount
            transactor_object.save()
            revolver_object.save()
            transactionrecord = transaction_record(
                transactor=transactor_object.cust_name,
                revolver=form.cleaned_data['revolver'],
                amount=form.cleaned_data['amount'])
            transactionrecord.save()
            return HttpResponseRedirect("/thank-you")

    else:
        single_customer = get_object_or_404(customer, slug=slug)
        form = transactForm()

    return render(request, 'sparks_bank/single-customer.html', {
        'name': single_customer.cust_name,
        'id': single_customer.cust_id,
        'form': form
    })

'''


def singlecustomer(request, slug):
    if request.method == "POST":
        transactor_object = get_object_or_404(customer, slug=slug)
        form = transactForm(request.POST)
       # revolver_object = get_object_or_404(customer, cust_name=request.POST.get("revolver"))
        amount = request.POST.get("amount")
        b = customer.objects.get(cust_name=request.POST.get("revolver"))
        b.current_balance = (b.current_balance + int(amount))
        b.save()

       # new_balance = transactor_object.current_balance - amount
       # transactor_object.current_balance = new_balance

        transaction = transaction_record(
            # transactor=request.POST.get("transactor"),
            transactor=transactor_object.cust_name,
            revolver=request.POST.get("revolver"),
            amount=request.POST.get("amount")
        )
        transaction.save()
        return HttpResponseRedirect("/thank-you")

    else:
        single_customer = get_object_or_404(customer, slug=slug)
        # single_customer = customer.objects.get()
        form = transactForm()

    return render(request, 'sparks_bank/singlecustomer.html', {
        'name': single_customer.cust_name,
        'id': single_customer.cust_id,
        'email': single_customer.cust_email,
        'balance': single_customer.current_balance,
        'form': form
    })


def transact(request, slug):
    if request.method == "POST":
        transactor_object = get_object_or_404(customer, slug=slug)
        form = transactForm(request.POST)
       # revolver_object = get_object_or_404(customer, cust_name=request.POST.get("revolver"))
        amount = request.POST.get("amount")
        b = customer.objects.get(cust_name=request.POST.get("revolver"))
        b.current_balance = (b.current_balance + int(amount))
        b.save()

       # new_balance = transactor_object.current_balance - amount
       # transactor_object.current_balance = new_balance

        transaction = transaction_record(
            # transactor=request.POST.get("transactor"),
            transactor=transactor_object.cust_name,
            revolver=request.POST.get("revolver"),
            amount=request.POST.get("amount")
        )
        transaction.save()
        return HttpResponseRedirect("/thank-you")

    else:
        single_customer = get_object_or_404(customer, slug=slug)
        # single_customer = customer.objects.get()
        form = transactForm()

    return render(request, 'sparks_bank/transact.html', {
        'name': single_customer.cust_name,
        'id': single_customer.cust_id,
        'email': single_customer.cust_email,
        'balance': single_customer.current_balance,
        'form': form
    })


def thank_you(request):
    customers = customer.objects.all()
    return render(request, 'sparks_bank/thank_you.html', {
        'customers': customers
    })


def transaction_history(request):
    transactions = transaction_record.objects.all()
    return render(request, 'sparks_bank/transaction-history.html', {
        'transactions': transactions
    })
