"""lit_review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import users.views
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup/", users.views.signup_page, name="signup"),
    path("logout/", users.views.logout_user, name="logout"),
    path("authenticate/", users.views.authenticate_page, name="authenticate"),
    path("", reviews.views.feed_page, name="feed"),
    path("myactivity/", reviews.views.my_activity_page, name="my-activity"),
    path("review/add/", reviews.views.add_ticket_and_review_page, name='add-ticket-and-review'),
    path("review/add/<int:ticket_id>/", reviews.views.add_review_page, name='add-review'),
    path("review/edit/<int:review_id>/", reviews.views.edit_review_page, name='edit-review'),
    path("ticket/add", reviews.views.add_ticket_page, name="add-ticket"),
    path('ticket/edit/<int:ticket_id>/', reviews.views.edit_ticket_page, name='edit-ticket'),
    path("follow/", users.views.follow_page, name="follow"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
