from django.urls import path
from knox import views as knox_views
from .views import RegisterAPI, LoginAPI
from knox import views as knox_views
from .views import (
    CursoListCreateView,
    CursoRetrieveUpdateDestroyView,
    DisciplinaListCreateView,
    DisciplinaRetrieveUpdateDestroyView,
    TurmaListCreateView,
    TurmaRetrieveUpdateDestroyView,
    FuncionarioListCreateView,
    FuncionarioRetrieveUpdateDestroyView,
    EstudanteListCreateView,
    EstudanteRetrieveUpdateDestroyView,
    DocenteListCreateView,
    DocenteRetrieveUpdateDestroyView
)

urlpatterns = [
    #login
    #path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),


    # Curso URLs
    path('cursos/', CursoListCreateView.as_view(), name='curso-list-create'),
    path('cursos/<int:pk>/', CursoRetrieveUpdateDestroyView.as_view(), name='curso-detail'),

    # Disciplina URLs
    path('disciplinas/', DisciplinaListCreateView.as_view(), name='disciplina-list-create'),
    path('disciplinas/<int:pk>/', DisciplinaRetrieveUpdateDestroyView.as_view(), name='disciplina-detail'),

    # Turma URLs
    path('turmas/', TurmaListCreateView.as_view(), name='turma-list-create'),
    path('turmas/<int:pk>/', TurmaRetrieveUpdateDestroyView.as_view(), name='turma-detail'),

    # Funcionario URLs
    path('funcionarios/', FuncionarioListCreateView.as_view(), name='funcionario-list-create'),
    path('funcionarios/<int:pk>/', FuncionarioRetrieveUpdateDestroyView.as_view(), name='funcionario-detail'),

    # Estudante URLs
    path('estudantes/', EstudanteListCreateView.as_view(), name='estudante-list-create'),
    path('estudantes/<int:pk>/', EstudanteRetrieveUpdateDestroyView.as_view(), name='estudante-detail'),

    # Docente URLs
    path('docentes/', DocenteListCreateView.as_view(), name='docente-list-create'),
    path('docentes/<int:pk>/', DocenteRetrieveUpdateDestroyView.as_view(), name='docente-detail'),
]


"""
from django.urls import path
from .views import (
    CursoListCreateView,
    CursoRetrieveUpdateDestroyView,
    DisciplinaListCreateView,
    DisciplinaRetrieveUpdateDestroyView,
    TurmaListCreateView,
    TurmaRetrieveUpdateDestroyView
)

urlpatterns = [
    # Curso URLs
    path('cursos/', CursoListCreateView.as_view(), name='curso-list-create'),
    path('cursos/<int:pk>/', CursoRetrieveUpdateDestroyView.as_view(), name='curso-detail'),

    # Disciplina URLs
    path('disciplinas/', DisciplinaListCreateView.as_view(), name='disciplina-list-create'),
    path('disciplinas/<int:pk>/', DisciplinaRetrieveUpdateDestroyView.as_view(), name='disciplina-detail'),

    # Turma URLs
    path('turmas/', TurmaListCreateView.as_view(), name='turma-list-create'),
    path('turmas/<int:pk>/', TurmaRetrieveUpdateDestroyView.as_view(), name='turma-detail'),
]

"""