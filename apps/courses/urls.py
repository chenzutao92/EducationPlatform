from django.conf.urls import url

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, VideoPlayView

urlpatterns = [
    # 课程列表
    url(r'^list/$', CourseListView.as_view(), name="courses_list"),

    #课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="courses_detail"),
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="courses_info"),
    # 评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="courses_comments"),
    # 添加评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name="add_comment"),
    # 课程学习地址
    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video_play"),

]
