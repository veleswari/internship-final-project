from django.urls import path
from Hospital import views
from django.contrib.auth import views as v

urlpatterns = [
	path('',views.home,name="hm"),
	
	path('rg/',views.usrreg,name="reg"),
	path('login/',v.LoginView.as_view(template_name="app/login.html"),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name="app/logout.html"),name="lgo"),
	path('adlist/',views.doclist,name="adstl"),
	path('docup/<int:m>/',views.docupd,name="dup"),
	path('docdt/<int:n>/',views.docdlt,name="ddt"),
	path('docvw/',views.docview,name="docv"),

	path('pdlist/',views.palist,name="pdstl"),
	path('pavw/',views.paview,name="pav"),
	path('patup/<int:m>/',views.patupd,name="pup"),
	path('patdt/<int:n>/',views.patdlt,name="pdt"),
	
	path('aplist/',views.aplist,name="apstl"),
	path('apvw/',views.apview,name="apv"),
	path('aptup/<int:m>/',views.aptupd,name="aup"),
	path('aptdt/<int:n>/',views.aptdlt,name="adt"),
]
