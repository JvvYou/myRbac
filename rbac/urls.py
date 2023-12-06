from django.urls import path, include
from .views import user, organization, menu, role, permission
from rest_framework import routers
from rest_framework_jwt import views

router = routers.DefaultRouter()
router.register(r'users', user.UserViewSet, basename="users")
router.register(r'organizations', organization.OrganizationViewSet, basename="organization")
router.register(r'menus', menu.MenuViewSet, basename="menus")
router.register(r'permissions', permission.PermissionViewSet, basename="permissions")
router.register(r'roles', role.RoleViewSet, basename="roles")

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'auth/info/', user.UserInfoView.as_view(), name='user_info'),
    path(r'auth/build/menus/', user.UserBuildMenuView.as_view(), name='build_menus'),  # 菜单列表
    path(r'api/organization/tree/', organization.OrganizationTreeView.as_view(), name='organizations_tree'),  # 组织架构树
    path(r'api/organization/user/tree/', organization.OrganizationUserTreeView.as_view(),
         name='organization_user_tree'),  # 部门用户树
    path(r'api/menu/tree/', menu.MenuTreeView.as_view(), name='menus_tree'),  # 菜单树
    path(r'api/permission/tree/', permission.PermissionTreeView.as_view(), name='permissions_tree'),  # 权限树
    path(r'api/user/list/', user.UserListView.as_view(), name='user_list'),
    path(r'auth/api-token/', views.obtain_jwt_token),
]
