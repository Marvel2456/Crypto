from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Wallet, Portfolio

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['email', 'username',  'password1', 'password2']


class CreateWalletForm(ModelForm):

    class Meta:
        model = Wallet
        fields = ['coin', 'quantity']
        exclude = ['owner',]

    def __init__(self, *args, **kwargs): 
        super(CreateWalletForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

        

# class PortfolioForm(ModelForm):

#     class Meta:
#         model = Portfolio
#         fields = ['']

        