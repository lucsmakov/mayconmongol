class User:
    def __init__(self, id, name, email, senha):
        self.id = id
        self.name = name
        self.email = email
        self.senha = senha
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'senha': self.senha
        }