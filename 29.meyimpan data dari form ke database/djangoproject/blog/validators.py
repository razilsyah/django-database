from django.core.exceptions import ValidationError


def validate_author(value):
    judul_input = value
    if judul_input == "einstein":
        message = 'maaf ' + judul_input + " tidak bisa di posting"
        raise ValidationError(message)
