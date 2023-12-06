1、参考 [drf_rbac](https://github.com/yance-dev/drf_rbac),增加了一些我想要的内容

2、settings_dev.py 文件参考
```python
from myRbac.settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xxxx',
        'USER': 'root',
        'PASSWORD': 'xxxxx',
        'HOST': '192.168.x.x',
        'PORT': '3306',
        # 单元测试数据库，用完释放
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci'
        },
        'OPTIONS': {
            "init_command": "SET foreign_key_checks = 0;",
        }
    }
}
```

3、jwt调用[参考](https://styria-digital.github.io/django-rest-framework-jwt/#overview)