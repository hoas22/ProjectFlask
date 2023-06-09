from app import db
from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token
from secrets import token_hex


class AuthController:
    def __init__(self):
        self.model = UserModel
        self.rol_id = 2

    def signIn(self, data):
        try:
            usuario = data['usuario']
            contrasena = data['contrasena']

            record = self.model.where(usuario=usuario, estado=True).first()
            if record:

                if record.checkContrasena(contrasena):

                    user_id = record.id
                    access_token = create_access_token(identity=user_id)
                    refresh_token = create_refresh_token(identity=user_id)
                    return {
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    }, 200
                else:
                    raise Exception('La contraseña es incorrecta')

            raise Exception('No se encontro el usuario')
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def signUp(self, data):
        try:
            data["rol_id"] = self.rol_id
            new_record = self.model.create(**data)
            new_record.hashContrasena()
            db.session.add(new_record)
            db.session.commit()
            return {
                'message': 'El usuario se creo con exito'
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'ocurrio un error',
                'error': str(e)
            }, 500
