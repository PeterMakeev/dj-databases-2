from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArticleTags


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class ArticleTagsInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                counter += 1
                continue
        if counter > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()


class ArticleTagsInline(admin.TabularInline):
    model = ArticleTags
    formset = ArticleTagsInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagsInline]