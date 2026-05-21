def require_auth(func):
    def wrapper(user):
        if user=="admin":
            return func(user)
        else:
            print("Usuario no activo")
    return wrapper

def admin_dashboard(user):
    return f"Bienvenido al dashboard, {user}"

auth_view_dashboar=require_auth(admin_dashboard)
print(auth_view_dashboar("admin"))
print(auth_view_dashboar("Adan"))