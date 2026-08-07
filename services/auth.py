import services.database as db

def register_user(username, email, password,password_confirm):

    if username == "" or email == "" or password == "" or password_confirm == "":
        return "empty_fields"
    
    if password != password_confirm:
        return "password_mismatch"

    if db.find_user_by_username(username) is not None:
        return "already_username"

    if db.find_user_by_email(email) is not None:
            return "already_email"

    db.insert_user(username,email,password)

    return "success"