from django.urls import path,include
from .views import * 
from . import views 

from rest_framework.routers import DefaultRouter 
from rest_framework.authtoken.views import obtain_auth_token

router1 = DefaultRouter()
router1.register("Niveau",views.Niveauviews, basename='niveau')
router1.register("Champ",views.ChampLexicaleViews, basename='champ')



router = DefaultRouter()
router.register("Champ",views.ChampLexicaleViews)
router.register('contenu',views.ContenuListviews, )
router.register('mot',views.Motfrviews)
router.register('traduire',views.Traduireviews)


urlpatterns = [
    path('langue/list/', ListLangue.as_view()),
    path('<int:pk>/langue/details', DetailLangue.as_view(), name= 'formation-detail'),
    path('langue/create/', CreateLangue.as_view()),
    path('<int:pk>/langue/delete/', DellLangue.as_view(), name='formation-dell'),
    path('<int:pk>/langue/update/', UpdateLangueView.as_view(), name='formation-update'),

    path('Niveau/',include(router1.urls)),

    path('champ/', ContenuListviews.as_view()),
    path('champ/create', ContenuCreatViews.as_view()),

    path('champ/<int:id_Contenir>', ContenuDetailViews.as_view()),

    path('auth', obtain_auth_token),

 ]
 