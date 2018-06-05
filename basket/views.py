from django.shortcuts import render
from basket.models import Player,Team,Coach,TeamCompose,Match
from basket.forms import PlayerForm,TeamForm,MatchForm,CoachForm,TeamComposeForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

def index(request):
    data = {
    }

    template_name = 'index.html'
    return render(request,template_name,data)

def player_list(request):
    data = {}

    # SELECT * FROM player
    object_list = Player.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'player/list_player.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def player_del(request,pk):
    player = Player.objects.get(pk=pk)
    player.delete()

    return HttpResponseRedirect(reverse("player_list"))

def player_add(request):
    data = {}
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES)
        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('player_list')

    else:
        data['form'] = PlayerForm()

    data["titulo"] = "Agregar"
    template_name = 'player/add_player.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def player_edit(request,pk):
    data = {}
    player = Player.objects.get(pk=int(pk))
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES, instance=player)
        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()
            return redirect('player_list')

    else:
        print("Este es el Player ", player)
        data['form'] = PlayerForm(instance=player)

    data["titulo"] = "Editar"
    template_name = 'player/add_player.html'
    return render(request, template_name, data)


def team_list(request):
    data = {}

    # SELECT * FROM player
    object_list = Team.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'team/list_team.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def team_del(request,pk):
    team = Team.objects.get(pk=pk)
    team.remove()

    return HttpResponseRedirect(reverse("team_list"))

def team_add(request):
    data = {}
    if request.method == "POST":
        data['form'] = TeamForm(request.POST, request.FILES)
        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('team_list')

    else:
        data['form'] = TeamForm()

    data["titulo"] = "Agregar"
    template_name = 'team/add_team.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def team_edit(request,pk):
    data = {}
    team = Team.objects.get(pk=int(pk))
    if request.method == "POST":
        data['form'] = TeamForm(request.POST, request.FILES, instance=team)
        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()
            return redirect('team_list')

    else:
        print("Este es el Team ", team)
        data['form'] = TeamForm(instance=Team)

    data["titulo"] = "Editar"
    template_name = 'team/add_team.html'
    return render(request, template_name, data)

def coach_list(request):
    data = {}

    # SELECT * FROM player
    object_list = Coach.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'coach/list_coach.html'
    return render(request, template_name, data)


@login_required(login_url='/auth/login')
def coach_del(request,pk):
    coach = Coach.objects.get(pk=pk)
    coach.delete()

    return HttpResponseRedirect(reverse("coach_list"))

def coach_add(request):
    data = {}
    if request.method == "POST":
        data['form'] = CoachForm(request.POST)
        username = request.POST["rut"]
        password = request.POST["nickname"]+request.POST["dv"]
        print("Esta esl a password: ",password)
        user = User.objects.create_user(username=username,password=password)
        user.save()
        if data['form'].is_valid():
            # aca el formulario valido
            coach=data['form'].save()
            coach.user = user
            coach.save()
            return redirect('coach_list')

    else:
        data['form'] = CoachForm()

    data["titulo"] = "Agregar"
    template_name = 'coach/add_coach.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def coach_edit(request,pk):
    data = {}
    coach = Coach.objects.get(pk=int(pk))
    if request.method == "POST":

        data['form'] = CoachForm(request.POST, instance=coach)
        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()
            return redirect('coach_list')

    else:
        print("Este es el Coach ", coach)
        data['form'] = CoachForm(instance=coach)

    data["titulo"] = "Editar"
    template_name = 'coach/add_coach.html'
    return render(request, template_name, data)

def teamcompose_list(request):
    data = {}

    # SELECT * FROM player
    object_list = TeamCompose.objects.filter(author=request.user.coach).order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'teamcompose/list_teamcompose.html'
    return render(request, template_name, data)


@login_required(login_url='/auth/login')
def teamcompose_del(request,pk):
    teamcompose = TeamCompose.objects.get(pk=pk)
    teamcompose.delete()

    return HttpResponseRedirect(reverse("teamcompose_list"))

@login_required(login_url='/auth/login')
def teamcompose_add(request):
    data = {}
    coach = request.user.coach
    if request.method == "POST":
        players = request.POST.get_list("players[]")
        match = request.POST["match"]
        match = Match.objects.get(pk=int(match))
        teamcompose = TeamCompose.objects.create(match=match)
        teamcompose.save()
        for player in players:
            player = Player.objects.get(pk=int(player))
            teamcompose.players.add(player)
            teamcompose.save()
        template_name = 'teamcompose/list_teamcompose.html'
        return render(request, template_name, data)

    else:
        players = Player.objects.filter(team=coach.team)
        matches = Match.objects.filter(Q(team1=coach.team) | Q(team2=coach.team))
        data["players"] = players
        data["matches"] = matches

    data["titulo"] = "Agregar"
    template_name = 'teamcompose/add_teamcompose.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def teamcompose_edit(request,pk):
    data = {}
    teamcompose = TeamCompose.objects.get(pk=int(pk))
    if request.method == "POST":
        data['form'] = TeamComposeForm(request.POST, request.FILES, instance=teamcompose)
        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()
            return redirect('player_list')

    else:
        print("Este es el TeamCompose ", teamcompose)
        data['form'] = TeamComposeForm(instance=teamcompose)

    data["titulo"] = "Editar"
    template_name = 'teamcompose/add_teamcompose.html'
    return render(request, template_name, data)

def match_list(request):
    data = {}

    # SELECT * FROM player
    object_list = Match.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'match/list_match.html'
    return render(request, template_name, data)


@login_required(login_url='/auth/login')
def match_del(request,pk):
    match = Match.objects.get(pk=pk)
    match.delete()

    return HttpResponseRedirect(reverse("match_list"))

def match_add(request):
    data = {}
    if request.method == "POST":
        data['form'] = MatchForm(request.POST, request.FILES)
        if data['form'].is_valid():
            # aca el formulario valido
            match = data['form'].save()
            match.date = request.POST["date"]
            match.save()
            return redirect('match_list')

    else:
        data['form'] = MatchForm()

    data["titulo"] = "Agregar"
    template_name = 'match/add_match.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def match_edit(request,pk):
    data = {}
    match = Match.objects.get(pk=int(pk))
    if request.method == "POST":
        data['form'] = MatchForm(request.POST, request.FILES, instance=match)
        if data['form'].is_valid():
            # aca el formulario valido
            match = data['form'].save()
            match.date = request.POST["date"]
            match.save()
            return redirect('match_list')

    else:
        print("Este es el Match ", match)
        data['form'] = MatchForm(instance=match)

    data["titulo"] = "Editar"
    template_name = 'match/add_match.html'
    return render(request, template_name, data)

def detail(request, player_id):

    data = {}
    template_name = 'player/detail_player.html'

    # SELECT * FROM player WHERE id = player_id
    data['player'] = Player.objects.get(pk=player_id)
    # import pdb;pdb.set_trace()

    return render(request, template_name, data)
