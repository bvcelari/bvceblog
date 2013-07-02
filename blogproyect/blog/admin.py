from blog.models import Post, Commentary
from django.contrib import admin
## TINY MCE 
from tinymce.widgets import TinyMCE
from django.core.urlresolvers import reverse
## END TINY MCE 

class CommentaryInline(admin.StackedInline):
  model = Commentary

class PostAdmin(admin.ModelAdmin):
  def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('content'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list'),},
            ))  
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)


  list_display = ('title', 'excerpt', 'publication_date', 'owner')
  list_filter = ['publication_date', 'owner']
  date_hierarchy = 'publication_date'
  search_fields = ['title', 'content', 'owner__username', 'owner__first_name', 'owner__last_name']
  prepopulated_fields = { 'machine_name' : ('title', ) }
  inlines = [CommentaryInline] 
admin.site.register(Post, PostAdmin)

 
class CommentaryAdmin(admin.ModelAdmin):
  list_display = ('author', 'post', 'publication_date')
  list_filter = ['publication_date', 'author']
  search_fields = ['author', 'content', 'blog__title']
 
admin.site.register(Commentary, CommentaryAdmin)
