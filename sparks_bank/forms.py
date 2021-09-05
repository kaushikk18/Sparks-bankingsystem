from django import forms


GEEKS_CHOICES = (
    ("Kaushik Ayyanar", "Kaushik Ayyanar"),
    ("Jeeva Mutharasi", "Jeeva Mutharasi"),
    ("Kiran kumar", "Kiran Kumar"),
    ("Akash Chopra", "Akash Chopra"),
    ("Vimal Kumar", "Vimal Kumar"),
    ("Kumar Ravi", "Kumar Ravi"),
    ("Priya Dharshini", "Priya Dharshini"),
    ("Dev Dayal", "Dev Dayal"),
    ("Jeevitha Sneha", "Jeevitha Sneha"),
    ("Siva Karthik", "Siva Karthik"),
)


class transactForm(forms.Form):
   # transactor = forms.CharField(max_length=43)
    revolver = forms.ChoiceField(choices=GEEKS_CHOICES, required=False,
                                 widget=forms.Select(attrs={'class': 'revolver'}))
    amount = forms.IntegerField(widget=forms.TextInput
                                (attrs={'class': 'amount', 'placeholder': 'In rupees'}))


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
        "required": "Your name must not be empty!",
        "max_length": "Please enter a shorter name!"
    })
    review_text = forms.CharField(
        label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
