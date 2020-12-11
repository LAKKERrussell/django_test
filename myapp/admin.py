from django.contrib import admin

# Register your models here.
from .models import log_move
from .models import PowerModel
from .models import UserInformationModel
from .models import UserModel
from django.contrib import admin

admin.site.site_header = '日志管理系统'  # 设置header
admin.site.site_title = 'down'          # 设置title
admin.site.register(log_move)
admin.site.register(PowerModel)
admin.site.register(UserInformationModel)
admin.site.register(UserModel)

