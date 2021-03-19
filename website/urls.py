from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('service.html', views.service, name="service"),
    path('cleaning.html', views.cleaning, name="cleaning"),
    path('missing.html', views.missing, name="missing"),
    path('whitening.html', views.whitening, name="whitening"),
    path('cosmetic.html', views.cosmetic, name="cosmetic"),
    path('tpain.html', views.tpain, name="tpain"),
    path('surgery.html', views.surgery, name="surgery"),
    path('credit.html', views.credit, name="credit"),
    path('lending.html', views.lending, name="lending"),
    path('insurance.html', views.insurance, name="insurance"),
    path('policy.html', views.policy, name="policy"),
    path('faqs.html', views.faqs, name="faqs"),
    path('privacy.html', views.privacy, name="privacy"),
    path('gallery.html', views.gallery, name="gallery"),

]