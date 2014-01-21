from django.shortcuts import render_to_response
from wiki.models import Article
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from forms import MyRegistrationForm
from forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.template import RequestContext


def wikis(request):
    return render_to_response('wikis.html',
                      {'wikis': Article.objects.filter(is_private=False)}, context_instance=RequestContext(request))


def wiki(request, wiki_id):
    return render_to_response('wiki.html',
                             {'wiki': Article.objects.get(id = wiki_id)},context_instance=RequestContext(request))


def mywikis(request):
    return render_to_response('mywikis.html',
                {'mywikis': Article.objects.filter(user=request.user)}, context_instance=RequestContext(request))


def mywiki(request, mywiki_id=1):
    return render_to_response('mywiki.html',
                             {'mywiki': Article.objects.get(id=mywiki_id)}, context_instance=RequestContext(request))


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    return render_to_response('loggedin.html', context_instance=RequestContext(request))


def invalid_login(request):
    return render_to_response('invalid.html')


def logout_view(request):
    logout(request)
    return redirect('/wikis/all/')


def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = MyRegistrationForm()
    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')


@login_required(login_url='/accounts/login/')
def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return HttpResponseRedirect('/wikis/all')

    else:
        form = ArticleForm()

        args = {}
        args.update(csrf(request))

        args['form'] = form
        return render_to_response('create_article.html', args)


@login_required(login_url='/accounts/login/')
def editwiki(request, wiki_id):
    wiki = Article.objects.get(id = wiki_id)
    editform = ArticleForm(request.POST or None, instance=wiki)
    if request.method == 'POST':
        if editform.is_valid():
            editform.save()
            return HttpResponseRedirect('/wikis/all')
    args = {}
    args.update(csrf(request))
    args['editform'] = editform
    return render_to_response('editwiki.html',
                         args, context_instance=RequestContext(request))


def like_wiki(request, wiki_id):
    if wiki_id:
        a = Article.objects.get(id=wiki_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()

    return HttpResponseRedirect('/wikis/get/%s' % wiki_id)
