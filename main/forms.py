# from django import forms
# from django.core.validators import RegexValidator
# from django.core.exceptions import ValidationError
# from .models import Reviews

# """
# from django import forms
# from .models import Item

# class AddForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ('created_by',
#         'title', 'image', 'description', 'price', 'pieces', 'instructions', 'labels', 'label_colour', 'slug')
#         """


# from django import forms
# from .models import Reviews
# from django.core.exceptions import ValidationError
# import re

# def validate_no_special_characters(value):
#     regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')  # regular expression to match special characters
#     if regex.search(value):
#         raise ValidationError("Special characters are not allowed")
    
# class ReviewForm(forms.Form):
#     review = forms.CharField(validators=[validate_no_special_characters])    

# # def validate_no_special_characters(value):
#     # """
#     # Validator function to check that a string doesn't contain special characters
#     # """
#     # if re.search('[^a-zA-Z0-9\s]', value):
#         # raise ValidationError(
#             # _("The input field should not contain any special characters."),
#             # code='no_special_characters',
#         # )
# # 
# # class ReviewForm(forms.ModelForm):
#     # review = forms.CharField(
#         # widget=forms.TextInput(attrs={
#             # 'class': 'form-control',
#             # 'placeholder': 'Enter Your Review'
#         # }), validators=[validate_no_special_characters]
#     # )
#     # rslug = forms.CharField(widget=forms.HiddenInput())
# # 
#     # class Meta:
#         # model = Reviews
#         # fields = ['review', 'rslug']
# # 
# # def validate_no_special_characters(rw):
#     # """
#     # Validator function to check that a string doesn't contain special characters
#     # """
#     # special_characters = '!@#$%^&*()_+-='
#     # if any(char in special_characters for char in rw):
#         # raise ValidationError(
#             # _("The input field should not contain any special characters."),
#             # code='no_special_characters',
#         # )    
#     # 
#     # 
# # 
# # class ReviewForm(forms.Form):
#     # review = forms.CharField(attrs={'class': 'form-control', 'placeholder': 'Enter Your Review'}, validators=[validate_no_special_characters])
# # 
#     # class Meta:
#         # model = Reviews
#         # fields = ['review', 'rslug']

#     # def clean_review(self):
#         # review = self.cleaned_data['review']
#         # pattern = re.compile('[^A-Za-z0-9 ]+')
#         # if pattern.search(review):
#             # raise ValidationError('Review contains invalid characters')
#         # return review
 

# # def validate_no_special_characters(value):
#     # if re.search(r'[^\w\s]', value):
#         # raise ValidationError('Special characters are not allowed.')
# # 
# # class ReviewForm(forms.Form):
#     # class Meta:
#         # model = Reviews
#         # fields = ['review']
#     # review = forms.CharField(max_length=200,widget=forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Enter your review here'}), validators=[validate_no_special_characters])
#     # rslug = forms.CharField(widget=forms.HiddenInput())
# # 
#     # def clean_review(self):
#         # data = self.cleaned_data['review']
#         # return re.sub(r'[^\w\s]', '', data)
















# # class ReviewForm(forms.Form):
#     # review = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Review'}))
#     # rslug = forms.CharField(widget=forms.HiddenInput())
# # 
#     # def clean_review(self):
#         # review = self.cleaned_data['review']
#         # validator = RegexValidator(r'^[a-zA-Z0-9 ]*$', 'Special characters are not allowed.')
#         # validator(review)
#         # return review