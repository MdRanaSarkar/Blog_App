from django.contrib import admin
from .models import Author, Category, Article, Amar, Commentd
# Register your models here
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    search_display = ["__str__"]
    class Meta:
        Model = Author

admin.site.register(Author, AuthorAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    search_display = ["__str__"]
    list_per_page = 10
    class Meta:
        Model=Category
admin.site.register(Category, CategoryAdmin)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    search_display = ["__str__"]
    list_per_page = 10
    list_filter = ["posted_on", "category"]
    class Meta:
        Model=Article
admin.site.register(Article, ArticleAdmin)


admin.site.register(Commentd)
admin.site.register(Amar)
