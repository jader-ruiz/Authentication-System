import services.database as db
import bcrypt

def register_user(username, email, password,password_confirm):

    if username == "" or email == "" or password == "" or password_confirm == "":
        return "empty_fields"
    
    elif password != password_confirm:
        return "password_mismatch"

    elif "@" not in email or "." not in email:
        return "invalid_email"

    elif db.find_user_by_username(username) is not None:
        return "already_username"

    elif db.find_user_by_email(email) is not None:
        return "already_email"

    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password_bytes, salt)

    db.insert_user(username,email,password_hash)

    return "success"

def login_user(username, password):
    if username == "" or password == "":
        return {
                "status": "empty_fields",
                "user": None
            }

    user = db.find_user_by_username(username)
    if user is not None:
        password_bytes = password.encode("utf-8")
        result = bcrypt.checkpw( password_bytes , user[3] )
        if result:
            return {
                "status": "success",
                "user": {
                    "id": user[0],
                    "username": user[1],
                    "email": user[2],
                }
            }
        else:
            return {
                "status": "wrong_password",
                "user": None
            }
    else:
        return {
                "status": "user_not_found",
                "user": None
            }

def edit_user(user_id,username, email):
    if username == "" or email == "":
        return "empty_fields"
    
    elif "@" not in email or "." not in email:
        return "invalid_email"

    elif db.find_other_user_by_username(username, user_id) is not None:
        return "already_username"

    elif db.find_other_user_by_email(email, user_id) is not None:
        return "already_email"

    db.update_user(user_id,username,email)

    return "success"

def change_password(user_id,current_password,new_password,new_password_confirm):
    if current_password == "" or new_password == "":
        return "empty_fields"
    elif new_password != new_password_confirm:
        return "password_mismatch"

    password_bytes = current_password.encode("utf-8")

    store_password = db.select_password(user_id)

    if not bcrypt.checkpw(password_bytes, store_password[0]):
        return "incorrect_password"
    else:
        password_bytes = new_password.encode("utf-8")
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt)

        db.update_password(user_id,password_hash)

        return "success"
            



    

    