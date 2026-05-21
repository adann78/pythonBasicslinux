def require_auth(func):
    def wrapper(user):
        if user.lower()=="admin":
            return func(user)
        else:
            print("Usuario no activo")
    return wrapper
@require_auth
def admin_dashboard(user):
    return f"Bienvenido al dashboard, {user}"

print(admin_dashboard("admin"))
print(admin_dashboard("Adan"))