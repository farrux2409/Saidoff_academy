

from django.core.validators import RegexValidator


uzbek_phone_validator = RegexValidator(
    regex=r'^\+998\s?\(\d{2}\)\s?\d{3}\s?\d{2}\s?\d{2}$',
    message="Telefon raqami +998 (XX) XXX XX XX formatida bo'lishi kerak."
)