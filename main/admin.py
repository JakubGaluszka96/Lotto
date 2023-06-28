from django.contrib import admin
from .models import BetList, Bet, Typing, LottoDraw, LottoDraws
# Register your models here.
admin.site.register(BetList)
admin.site.register(Bet)
admin.site.register(Typing)
admin.site.register(LottoDraw)
admin.site.register(LottoDraws)

