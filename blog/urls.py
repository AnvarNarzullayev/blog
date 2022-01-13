from django.urls import path
from .views import blog,search, blogDetail, TagView, CategoryDetailView , CreateBlog ,Categorylist, UpdateBlog , DeleteBlog, Privacy

urlpatterns = [
    path('', blog, name="blog"),
    path('detail/<slug:slug_name>', blogDetail, name="detail"),
    path('tags/<slug:slug_tag>',TagView, name = 'tags'),
    path('category/<slug:slug>', CategoryDetailView.as_view(), name='category_detail'),
    path('CreateBlog/',CreateBlog.as_view(),name='create'),
    path('Category/',Categorylist.as_view(), name = 'Category'),
    path('Update/<slug:slug>',UpdateBlog.as_view(),name = 'update'),
    path('delete/<slug:slug>',DeleteBlog.as_view(),name = 'delete'),
    path('Xavfsizlik',Privacy,name = 'privacy'),
    path('search',search, name='product_search'),
]