При скачивании необходимо:
1. Установить все из requiremets:
2. Нужно в файле 'snowpenguin.django.recaptcha3.fields' заменить стандартный 'from django.utils.translation import ugettext_lazy as _' на 
'from django.utils.translation import gettext_lazy as _' и тогда все заработает
