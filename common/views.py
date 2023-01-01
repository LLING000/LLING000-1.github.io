from django.shortcuts import render
from .models import *
import json

def toLogin_view(request):
    artist = BestArtist.objects.all()
    data_sum = {}
    data_month = {}
    keys = list(BestArtist.objects.values_list('artist_id', flat=True))
    values_songs = list(BestArtist.objects.values_list('amount', flat=True))
    for k, v in zip(keys, values_songs):
        data_sum.update({k: v, }, )
    return render(request, 'index.html',{'month': json.dumps(keys), 'data': json.dumps(values_songs), 'data_sum': json.dumps(data_sum)})
