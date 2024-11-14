from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label='Full Name', help_text="Total length must be 10 characters", required=False, disabled=False, widget=forms.Textarea(attrs= {'id' : 'text_area', 'placeholder' : 'Enter your name'}))
    # file = forms.FileField()
    email = forms.EmailField(label='User Email')
    # age = forms.IntegerField()
    # weith = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs= {'type' : 'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))
    CHOISES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOISES, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'),  ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    
    
# class StudentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.EmailField()
    
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 5:
#             raise forms.ValidationError("Enter a name with at least 10 character")
#         if '.com' not in valemail:
#             raise forms.ValidationError('Enter a valid email')


class StudentForm(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(5, message='Enter a name with at least 10 character')])
    email = forms.EmailField(validators=[validators.EmailValidator(message='Enter a valid email')])
    
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message='age must be under 34'),validators.MinValueValidator(24, message='age must be atleast 24')])
    
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'])])
    

class PasswordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_pasword = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_pasword']
        val_name = self.cleaned_data['name']
        
        if val_pass != val_conpass:
            raise forms.ValidationError('Password doesn''t match')
        if len(val_name) < 5:
            raise forms.ValidationError('name too short')