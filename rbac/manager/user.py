from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, mobile=None, username=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            mobile=mobile,
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, mobile=None, username=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
            mobile=mobile
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user