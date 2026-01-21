import os

def bootstrap_admin_user():
    from VJISS_APP.models import Create_User

    email = os.getenv("DJANGO_ADMIN_EMAIL")
    first_name = os.getenv("DJANGO_ADMIN_FIRST_NAME")
    phone = os.getenv("DJANGO_ADMIN_PHONE")
    dob = os.getenv("DJANGO_ADMIN_DOB")
    password = os.getenv("DJANGO_ADMIN_PASSWORD")

    if not email or not password:
        return

    if Create_User.objects.filter(email=email).exists():
        return

    Create_User.objects.create_superuser(
        email=email,
        first_name=first_name,
        phone_number=phone,
        date_of_birth=dob,
        password=password,
    )

    print("✔ Admin user created successfully")
