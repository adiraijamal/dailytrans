from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Daily
from django.db.models import Q, Sum


# Create your views here.


def bymonth(request):
    ms = {
        'monjc': Daily.objects.aggregate(mjc=Sum('transamount',
                                                 filter=Q(transdate__month=1) & Q(transmode__name='Cash')
                                                 )
                                         )['mjc'],
        'monfc': Daily.objects.aggregate(mfc=Sum('transamount',
                                                 filter=Q(transdate__month=2) & Q(transmode__name='Cash')
                                                 )
                                         )['mfc'],
        'monje': Daily.objects.aggregate(mje=Sum('transamount',
                                                 filter=Q(transdate__month=1) & Q(transmode__name='ENBD')
                                                 )
                                         )['mje'],
        'monfe': Daily.objects.aggregate(mfe=Sum('transamount',
                                                 filter=Q(transdate__month=2) & Q(transmode__name='ENBD')
                                                 )
                                         )['mfe'],
    }
    print(ms)
    return render(request, 'bymonth.html', ms)


def index(request):
    translist = Daily.objects.all()
    template = loader.get_template('index.html')
    context = {
        'transactions': translist
    }
    return HttpResponse(template.render(context, request))