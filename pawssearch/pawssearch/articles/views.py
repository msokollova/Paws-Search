from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test

from .forms import ArticleForm
from .models import Article


# Check if user is staff
def is_staff(user):
    return user.is_staff


# List of articles
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article/all_article.html', {'articles': articles})


# Add new article (staff only)
@user_passes_test(is_staff)
def article_add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all article')
    else:
        form = ArticleForm()
    return render(request, 'article/form_article.html', {'form': form, 'action': 'Add'})


# Edit existing article (staff only)
@user_passes_test(is_staff)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('all article')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article/form_article.html', {'form': form, 'action': 'Edit'})


# Delete an article (staff only)
@user_passes_test(is_staff)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('all article')
    return render(request, 'article/article_confirm_delete.html', {'article': article})
