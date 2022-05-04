from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Regime, Election, Dictateur
from django.template import loader
from django.urls import reverse
from PIL import Image
# from westerosDictator import election


# Create your views here.
def index(request):
    derniere_election = Election.objects.order_by('id')
    context = {'election_list': derniere_election}
    return render(request, 'election/index.html', context)
    

def detail(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    return render(request, 'election/detail.html', {'election':election})


def liste(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    return render(request, 'election/liste.html', {'election':election})


def resultats(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    return render(request, 'election/resultats.html', {'election':election})


def vote(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    try:
        dictateur_choisi = election.dictateur_set.get(pk=request.POST['dictateur'])
    except (KeyError, Dictateur.DoesNotExist):
        return render(request,'election/detail.html', {'election':election, 
                                                        'error_message':'Veuillez selectionner un dictateur !',})
    
    else:
        dictateur_choisi.votes += 1
        dictateur_choisi.save()
        return HttpResponseRedirect(reverse('election:resultats', args=(election_id,)))


