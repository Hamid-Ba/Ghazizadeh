from django.urls import (
    path,
)

from siteinfo import views

app_name = "site_info"

urlpatterns = [
    path("about_us/", views.AboutUsView.as_view(), name="about_us"),
    path("contact_us/", views.ContactUsView.as_view(), name="contact_us"),
    path("home_header/", views.HomeHeaderView.as_view(), name="home_header"),
    path("footer/", views.FooterView.as_view(), name="footer"),
    path(
        "slider_and_banner/",
        views.SliderAndBannerView.as_view(),
        name="slider_and_banner",
    ),
]
