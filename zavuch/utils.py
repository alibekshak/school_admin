from django.forms import ValidationError


def validate_phone_namber(phone_number: str):
    phone_number = phone_number.replace(" ", "")
    if len(phone_number) < 12:
        raise ValidationError('Номер не правильный')

    if not phone_number.startswith("+"):
        raise ValidationError("Номер начинается с +")

    numbers = "+0123456789"
    for i in phone_number:
        if i not in numbers:
            raise ValidationError(f"Телефонный номер не может содержать {i} !")

