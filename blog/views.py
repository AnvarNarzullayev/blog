from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Blog, Category , Comment , MyUser
from django.views.generic import ListView, DetailView, CreateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import CreateBlogForm , CommentForm
from .filters import OrderFilter
from django.core.paginator import Paginator
from hitcount.views import HitCountDetailView
from django.urls import reverse



def blog(request):
    blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    MyFilter = OrderFilter(request.GET, queryset=blogs)
    blogs = MyFilter.qs
    cnt = Blog.objects.filter().order_by('-views')[:5]
    context = {
        "blogs": page_obj,
        "cnt":cnt,
        "filter":blogs,
        "myfilter":MyFilter
    }
    return render(request, 'blog.html', context)

# class BlogListView(ListView):
#     model = Blog
#     template_name = 'blog.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         blogs = Blog.objects.all().order_by('-created_at')
#         paginator = Paginator(blogs, 6)
#         page_number = self.request.GET.get('page')
#         page_obj = paginator.get_page(page_number)        
#         cnt = Blog.objects.filter().order_by('-views')[:5]
#         context['blogs'] = page_obj
#         context['cnt'] = cnt
#         context['filter'] = OrderFilter(self.request.GET, queryset = self.get_queryset())
#         return context

def blogDetail(request, slug_name):
    blog = Blog.objects.get(slug=slug_name)
    bogs_author = Blog.objects.filter(user_id=blog.user_id)
    blog_filter_category = Blog.objects.filter(category_id=blog.category_id)[:3]
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form_comment = form.save(commit = False)
            form_comment.user_id = request.user
            form_comment.blog_id = blog
            form_comment.save()
            return redirect('detail', slug_name = blog.slug)
    else:
        form = CommentForm()
    blog.views += 1
    blog.save()
    context = {
        'blog': blog,
        'blogs_author': bogs_author,
        'blog_flt_ctry': blog_filter_category,
        'form':form
    }
    return render(request, "detail.html", context)

# def blogDetail(request,slug_blog):
#     item = Blog.objects.all()
#     blog = Blog.objects.get(slug=slug_blog)
#     blogs_author = Blog.objects.filter(user_id=blog.user_id).order_by('views')[:5]
#     blogs_item = Blog.objects.filter(category_id=blog.category_id).order_by('views')[:3]
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form_comment = form.save(commit = False)
#             form_comment.user_id = request.user
#             form_comment.blog_id = blog
#             form_comment.save()
#             return redirect('detail', slug_blog = blog.slug)
#     else:
#         form = CommentForm()
#     blog.views+=1
#     blog.save()
#     return render(request,'detail.html',{'blog':blog,'item':item,'blogs_author':blogs_author,"blogs_item":blogs_item,'form':form})

# class BlogDetailView(DetailView):
#     model = Blog
#     template_name = 'detail.html'
#     form = CommentForm

#     def post(self, request, *args, **kwargs):        
#         slug = self.kwargs.get('slug')
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             blog = self.get_object()
#             form.instance.user_id = request.user
#             form.instance.blog_id = blog
#             form.save()

#             return redirect(reverse('detail', kwargs={
#                 'slug':blog.slug
#             }))

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)                
#         slug = self.kwargs.get('slug')
#         context['form'] = self.form
#         context['item'] = Blog.objects.all()
#         blog = Blog.objects.get(slug=slug)
#         context['blogs_author'] = Blog.objects.filter(user_id=blog.user_id).order_by('views')[:5]
#         context['blogs_item'] = Blog.objects.filter(category_id=blog.category_id).order_by('views')[:3]
#         blog.views+=1
#         blog.save()
#         context['blog'] = blog
        
#         return context

def TagView(request, slug_tag):
    blogs = Blog.objects.filter(tag__slug=slug_tag)
    return render(request, "blog.html", {'filter': blogs})

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_blog.html'
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['blogs'] = Blog.objects.filter(category_id__slug=slug)
        context['blog_count'] = Blog.objects.filter(category_id__slug=slug).count()
        context['blogs_top'] = Blog.objects.filter().order_by('views')[:5]
        context['categories'] = Category.objects.all()
        
        return context

class CreateBlog(LoginRequiredMixin,CreateView):
    form_class = CreateBlogForm
    template_name = 'Create_blog.html'
    success_url = reverse_lazy('blog')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

class Categorylist(ListView):
    model = Category
    template_name = 'Category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        blogs = Category.objects.all()
        paginator = Paginator(blogs, 6)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['category'] = page_obj

        return context


class UpdateBlog(UpdateView):
    model = Blog
    template_name = 'UpdateBlog.html'
    fields = ['name','slug','description','img','category_id','tag',]
    get_absolute_url = 'blog'

class DeleteBlog(DeleteView):
    model = Blog
    template_name = 'DeleteBlog.html'
    success_url = reverse_lazy('blog')


def Privacy(request):
    return render(request, 'Xavfsizlik.html')