from django.urls import path
from. import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about, name = 'about'),
    path('finches/', views.finches_index, name= 'index'),
    path('finches/<int:finch_id>/',views.finch_detail, name = 'detail'),
    path('finches/create/', views.FinchCreate.as_view(), name = 'finches_create'),
    path('finches/<int:pk>/update/',views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/',views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/',views.add_feeding,name='add_feeding'),

    path('cages/', views.CageList.as_view(), name='cages_index'),
    path('cages/<int:pk>/', views.CageDetail.as_view(), name='cages_detail'),
    path('cages/create/', views.CageCreate.as_view(), name='cages_create'),
    path('cages/<int:pk>/update/', views.CageUpdate.as_view(), name='cages_update'),
    path('cages/<int:pk>/delete/', views.CageDelete.as_view(), name='cages_delete'),
    path('finches/<int:finch_id>/assoc_cage/<int:cage_id>/', views.assoc_cage, name='assoc_cage'),
    path('finches/<int:finch_id>/unassoc_cage/<int:cage_id>/', views.unassoc_cage, name='unassoc_cage'),

]
