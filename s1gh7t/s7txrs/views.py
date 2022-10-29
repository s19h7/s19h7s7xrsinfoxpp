# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class S1gh7ts7txrHome(DataMixin, ListView):
    model = S1gh7ts7txr
    template_name = 's7txrs/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Home'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Home")
        context.update(c_def)
        return context

    def get_queryset(self):
        return S1gh7ts7txr.objects.filter(is_published=True).select_related('cat')


# def index(request):
#     posts = S1gh7ts7txr.objects.filter(is_published=True)
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Main pg',
#         'cat_selected': 0
#     }
#     return render(request, 's7txrs/index.html', context=context)

class ShowPost(DataMixin, DetailView):
    model = S1gh7ts7txr
    template_name = 's7txrs/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        context.update(c_def)
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(S1gh7ts7txr, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 's7txrs/post.html', context=context)


class S1gh7ts7txrCategory(DataMixin, ListView):
    model = S1gh7ts7txr
    template_name = 's7txrs/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return S1gh7ts7txr.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Category: ' + str(c.name),
                                      cat_selected=c.pk)
        context.update(c_def)
        return context


# def show_category(request, cat_slug):
#     cat_id = Category.objects.get(slug=cat_slug).pk
#     posts = S1gh7ts7txr.objects.filter(cat_id=cat_id)
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'view by categories',
#         'cat_selected': cat_id,
#     }
#     return render(request, 's7txrs/index.html', context=context)


def info(request):
    contact_list = S1gh7ts7txr.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 's7txrs/info.html', {'page_obj': page_obj, 'menu': menu, 'title': 'Info'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 's7txrs/addpage.html'
    login_url = reverse_lazy('home')

    # success_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add page")
        context.update(c_def)
        return context


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 's7txrs/addpage.html', {'form': form, 'menu': menu, 'title': 'Add page'})


# def feedback(request):
#     return HttpResponse(menu[2]['title'])\
class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 's7txrs/feedback.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Feedback")
        context.update(c_def)
        return context
    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

# def login(request):
#     return HttpResponse('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>куколд с рогами олень чмо-педофил</h1><p>бесы демоны упыри великаны гиганты</p>')


class SignupUser(DataMixin, CreateView):
    form_class = SignupForm
    template_name = 's7txrs/signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sign up")
        context.update(c_def)
        return context
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 's7txrs/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Log in")
        context.update(c_def)
        return context

    def get_success_url(self):
        return reverse_lazy('home')
def logout_user(request):
    logout(request)
    return redirect('login')
