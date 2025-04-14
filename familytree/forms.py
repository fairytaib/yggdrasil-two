from django import forms
from .models import Person
from datetime import date
from django.core.exceptions import ValidationError
from PIL import Image
import re


def validate_name_field(value, field_label="This field"):
    """Validates a name-like field: no numbers or special characters."""
    value = value.strip()
    
    if not value:
        return value

    pattern = r"^[a-zA-ZäöüÄÖÜß'\- ]+$"

    if not re.match(pattern, value):
        raise ValidationError(
            f"{field_label} must not contain numbers or special characters.")
    return value


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = (
            'featured_image', 'first_name', 'last_name',
            'birth_place', 'birth_country',
            'language', 'occupation', 'hobbies', 'nickname',
            'birth_date', 'death_date', 'bio'
        )

        widgets = {
            'featured_image': forms.FileInput(
                attrs={'class': 'form-control-file'}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'death_date': forms.DateInput(attrs={'type': 'date'}),
            'language': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'language':
                field.widget.attrs['class'] = 'form-control'
        self.fields['featured_image'].widget.attrs['class'] = 'form-control-file'

    def clean(self):
        cleaned_data = super().clean()
        strip_fields = ['first_name',
                        'last_name',
                        'occupation',
                        'hobbies',
                        'nickname']

        for field in strip_fields:
            value = cleaned_data.get(field)
            if value:
                cleaned_data[field] = value.strip()

    def clean_featured_image(self):
        image = self.cleaned_data.get('featured_image')

        if not image or not hasattr(image, 'file') or image.size == 0:
            return None

        try:
            img = Image.open(image)
            img.verify()
        except Exception:
            raise ValidationError("Uploaded file is not a valid image.")

        allowed_types = ['jpeg', 'png', 'gif', 'jpg', 'webp']
        if img.format.lower() not in allowed_types:
            raise ValidationError(
                f"Only {', '.join(allowed_types)} images are allowed.")

        return image

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date and birth_date > date.today():
            raise forms.ValidationError("Birth date cannot be in the future.")
        return birth_date

    def clean_death_date(self):
        death_date = self.cleaned_data.get('death_date')
        birth_date = self.cleaned_data.get('birth_date')
        if death_date and birth_date and death_date < birth_date:
            raise forms.ValidationError(
                "Death date cannot be before birth date.")
        if death_date and death_date > date.today():
            raise forms.ValidationError(
                "Death date cannot be in the future.")
        return death_date

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return validate_name_field(first_name, "First name")

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        return validate_name_field(last_name, "Last name")

    def birth_place(self):
        birth_place = self.cleaned_data.get('birth_place')
        return validate_name_field(birth_place, "Birth place")

    def clean_occupation(self):
        occupation = self.cleaned_data.get('occupation')
        return validate_name_field(occupation, "Occupation")

    def clean_hobbies(self):
        hobbies = self.cleaned_data.get('hobbies')
        return validate_name_field(hobbies, "Hobbies")

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        return validate_name_field(nickname, "Nickname")
