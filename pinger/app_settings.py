from django.conf import settings

CT_PINGER_VALID_STATES = getattr(settings, 'CT_PINGER_VALID_STATES', ["Member"])

CT_PINGER_FUEL_THRESHOLD = getattr(settings, 'CT_PINGER_FUEL_THRESHOLD', 15)
