# coding:utf-8
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import UserInfo, RoleList, PermissionList
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def permission_verify():
    """
        权限认证模块,
        此模块会先判断用户是否是管理员（is_superuser为True），如果是管理员，则具有所有权限,
        如果不是管理员则获取request.user和request.path两个参数，判断两个参数是否匹配，匹配则有权限，反之则没有。

        --------
        by zhouzx
        https://www.thinksaas.cn/group/topic/433334/

        进入项目环境终端命令：
        python manage.py shell
        使用django-admin shell报错


        ------
        Sqlite 中存储布尔类型问题：
        使用Navicat Premium查看
        使用python manage.py shell查看False True使用unicode编码的。
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            iUser = UserInfo.objects.get(username=request.user)
            # 判断用户如果是超级管理员则具有所有权限
            if not iUser.is_superuser==u'True':        # 转换unicode编码 by zhouzx
                if not iUser.role:  # 如果用户无角色，直接返回无权限
                    return HttpResponseRedirect(reverse('permission_deny'))     # url （u'/accounts/permission/deny/'）

                role_permission = RoleList.objects.get(name=iUser.role)
                role_permission_list = role_permission.permission.all()

                matchUrl = []
                for x in role_permission_list:
                    # 精确匹配，判断request.path是否与permission表中的某一条相符
                    # by zhouzx
                    # https://simpleisbetterthancomplex.com/tips/2016/07/20/django-tip-7-how-to-get-the-current-url-within-a-django-template.html
                    # s.rstrip(rm)      删除s字符串中结尾处，位于 rm删除序列的字符
                    # request.path ???
                    if request.path == x.url or request.path.rstrip('/') == x.url:
                        matchUrl.append(x.url)
                    # 判断request.path是否以permission表中的某一条url开头
                    elif request.path.startswith(x.url):
                        matchUrl.append(x.url)
                    else:
                        pass

                print('{}---->matchUrl:{}'.format(request.user, str(matchUrl)))
                if len(matchUrl) == 0:
                    return HttpResponseRedirect(reverse('permission_deny'))
            else:
                pass

            return view_func(request, *args, **kwargs)
        return _wrapped_view

    return decorator


@login_required
def permission_deny(request):
    return render(request, 'accounts/permission_deny.html')