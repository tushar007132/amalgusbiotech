
from django.contrib import admin
from django.urls import path, include
from post import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('home',views.home1,name="homeurl"),
    path('login',views.login,name="login"),
    path('submitlogin/',views.afterlogin,name="afterlogin"),
    path('blog/',views.blog,name="blog"),
    path('products/',views.products,name="products"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('contactus/',views.contactus,name="contactus"),
    path('contactus/submit/',views.submit,name="submit")

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
