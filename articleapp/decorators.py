from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_article = Article.objexts.get(pk=kwargs['pk'])
        if target_article.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated