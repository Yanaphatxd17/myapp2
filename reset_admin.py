import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp1.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_or_reset_admin():
    User = get_user_model()
    username = 'admin'
    email = 'yxmmiyanphathn@gmail.com'
    password = '190150zZxX'  # You can change this password to whatever you want

    u, created = User.objects.get_or_create(username=username, defaults={'email': email})
    u.set_password(password)
    u.is_superuser = True
    u.is_staff = True
    u.save()

    if created:
        print(f"SUCCESS: Created superuser '{username}' with password '{password}'")
    else:
        print(f"SUCCESS: Reset password for existing superuser '{username}' to '{password}'")

if __name__ == '__main__':
    create_or_reset_admin()
