from django.conf.urls import url
from . import views

urlpatterns=[
    url(r"^$",views.anasayfa, name="anasayfa"),
    url(r"^post/(?P<id>\d+)/duzenle/$",views.post_düzenle,name="duzenle"),
    url(r'^post/(?P<id>\d+)/$',views.icerik,name="icerik"),
    url(r"^post/add/$",views.yeni_post,name="yeni_post"),
    url(r"^post/(?P<id>\d+)/sil/$",views.sil,name="sil"),
    url(r"^kayit/$", views.kayit, name="kayit"),
    url(r"^giris/$",views.giris, name="giris"),
    url(r"^cıkıs/$",views.cıkıs,name="cıkıs"),
]
