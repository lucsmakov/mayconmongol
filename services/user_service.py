from models.user import User

users = []
id_user = 0

def id_generator():
    global id_user
    id_user += 1
    return id_user

def create_user(info):
    global users
    for x in users:
        if x.email == info['email']:
            return None, "the email already exists"
    new_user = User(id_generator(), info['name'], info['email'], info['senha'])
    users.append(new_user)
    return new_user, None

def user_list():
    #resultado = []
    #for user in users:
    #resultado.append(user.to_dict())
    #or
    #list = [x.to_dict() for x in users]
    #return list
    return [x.to_dict() for x in users]

def chosen_user_list(id):
    for x in users:
        if x.id == id:
            return x, None
    return None, "user not found"

def update_user(id, new_info):
    user_found, erro = chosen_user_list(id)
    if erro:
        return None, erro
    for x in users:
        if x.email == new_info['email'] and x.id != id:
            return None, "the email already exists"
    if user_found:
        user_found.name = new_info['name'] if 'name' in new_info else user_found.name
        user_found.email = new_info['email'] if 'email' in new_info else user_found.email
        user_found.senha = new_info['senha'] if 'senha' in new_info else user_found.senha
        return user_found, None
    if not new_info['name'] or new_info['email'] or new_info['senha']:
        return None, "bad request"

def delete_user(id):
    global users
    user, erro = chosen_user_list(id)
    if user:
        users.remove(user)
        return True, None
    if erro:
        return False, erro
        