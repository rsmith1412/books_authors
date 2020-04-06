from django.conf.urls import url
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_book$', views.add_book),
    url(r'^books/(?P<id>\d+)$', views.show_book),
    url(r'^add_author_to_book/(?P<id>\d+)$', views.add_author_to_book),
    url(r'^authors$', views.authors),
    url(r'^authors/(?P<id>\d+)$', views.show_author),
    url(r'^add_book_to_author/(?P<id>\d+)$', views.add_book_to_author),
]