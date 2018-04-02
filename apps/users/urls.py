from django.conf.urls import url
from .views import UserinfoView, UpdatePwdView, UploadImageView, SendEmailCodeView, UpdateEmailView
from .views import MyCourseView, MyFavOrgView, MyFavTeacherView, MyFavCourseView, MymessageView

urlpatterns = [
    # 课程列表
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),

    # 更新密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),

    # 送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),

    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

    # 我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),

    # 我收藏的课程机构
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),

    # 我收藏的授课教师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),

    # 我收藏的课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),

    # 我收藏的课程
    url(r'^mymessage/$', MymessageView.as_view(), name="mymessage"),

]
