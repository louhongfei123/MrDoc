from django.urls import path,re_path
from app_doc import views,util_upload_img

urlpatterns = [
    path('',views.project_list,name='pro_list'),# 文档首页
    #################文集相关
    path('project/<int:pro_id>/', views.project_index, name='pro_index'),  # 文集浏览页
    path('create_project/', views.create_project, name='create_project'),  # 新建文集
    path('get_pro_doc/', views.get_pro_doc, name="get_pro_doc"),  # 获取某个文集的下级文档
    path('modify_pro/',views.modify_project,name='modify_project'), # 修改文集

    #################文档相关
    path('project/<int:pro_id>/<int:doc_id>/', views.doc, name='doc'),  # 文档浏览页
    path('create_doc/', views.create_doc, name="create_doc"),  # 新建文档
    path('modify_doc/<int:doc_id>/', views.modify_doc, name="modify_doc"),  # 修改文档
    path('del_doc/<int:doc_id>/',views.del_doc,name="del_doc"), # 删除文档
    #################文档模板相关
    path('create_doctemp/',views.create_doctemp,name="create_doctemp"), # 创建文档模板
    ################其他功能相关
    path('upload_doc_img/',util_upload_img.upload_img,name="upload_doc_img"), # 上传图片
]