# coding:utf-8
from django import forms
from django.contrib import auth
from models import UserInfo, RoleList, PermissionList

class LoginUserForm(forms.Form):
    username = forms.CharField(label=u'账号', error_messages={'required': u'账号不能为空'},
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=u'密码', error_messages={'required': u'密码不能为空'},
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None

        super(LoginUserForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = auth.authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(u'账号密码不匹配')
            elif not self.user_cache.is_active:
                raise forms.ValidationError(u'此账号已被禁用')
        return self.cleaned_data


    def get_user(self):
        return self.user_cache




class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('username', 'email', 'nickname', 'role', 'is_active')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:500px;'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:500px;'}),
            'nickname': forms.TextInput(attrs={'class':'form-control', 'style': 'width:500px;'}),
            'role': forms.Select(attrs={'class': 'form-control', 'style': 'width:500px;'}),
            'is_active': forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class': 'form-control', 'style': 'width:500px;'}),
        }

    def __init__(self,*args,**kwargs):
        super(EditUserForm,self).__init__(*args,**kwargs)
        self.fields['username'].label = u'账 号'
        self.fields['username'].error_messages = {'required':u'请输入账号'}
        self.fields['email'].label = u'邮 箱'
        self.fields['email'].error_messages = {'required':u'请输入邮箱','invalid':u'请输入有效邮箱'}
        self.fields['nickname'].label = u'姓 名'
        self.fields['nickname'].error_messages = {'required':u'请输入姓名'}
        self.fields['role'].label = u'角 色'
        self.fields['is_active'].label = u'状 态'

    def clean_password(self):
        return self.cleaned_data['password']