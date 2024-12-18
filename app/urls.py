from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import (
    AssentoViewSet,
    CarrinhoViewSet,
    CategoriaViewSet,
    FilmeViewSet,
    IngressoViewSet,
    SalaViewSet,
    SessaoViewSet,
    TipoAssentoViewSet,
    UserViewSet,
)

router = DefaultRouter()

router.register(r"usuarios", UserViewSet, basename="usuarios")
router.register(r"categorias", CategoriaViewSet, basename="categorias")
router.register(r"tipos-assentos", TipoAssentoViewSet, basename="tipos-assentos")
router.register(r"filmes", FilmeViewSet, basename="filmes")
router.register(r"salas", SalaViewSet, basename="salas")
router.register(r"assentos", AssentoViewSet, basename="Assentos")
router.register(r"sessoes", SessaoViewSet, basename="sessoes")
router.register(r"ingressos", IngressoViewSet, basename="ingressos")
router.register(r"carrinhos", CarrinhoViewSet, basename="carrinhos")

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # Simple JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # API
    path("api/", include(router.urls)),
]
