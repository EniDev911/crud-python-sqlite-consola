class Cliente:

    def __init__(self, nombre, apellido, tel, direccion, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = tel
        self._email = '{}.{}@gmail.com'.format(nombre, apellido)
        self.direccion = direccion
        self.ciudad = ciudad

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def nombre_completo(self):
        return '{} {}'.format(self.nombre, self.apellido)

    def __repr__(self):
        return "Cliente('{}', '{}', '{}', '{}', '{}')".format(
            self.nombre,
            self.apellido,
            self.telefono,
            self.direccion,
            self.ciudad)
