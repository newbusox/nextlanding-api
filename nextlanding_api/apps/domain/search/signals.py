from django.dispatch import Signal

potential_search_completed = Signal(providing_args=['instance'])
apartment_added_to_search = Signal(providing_args=['instance', 'apartment'])
