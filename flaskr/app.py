from flaskr import create_app
from .models import db, Cancion, Album, Medio, Usuario
from .models import AlbumSchema, CancionSchema, UsuarioSchema
from flask_restful import Api
from .vistas import VistaCanciones, VistaCancion

app = create_app('default')

# Context is a dictionary that is used to store application-specific data.

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones, '/canciones/')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>/')

#Prueba
with app.app_context():
    pass

    # u = Usuario(nombre='Juan', contrasena='12345')
    # a = Album(titulo='Prueba', anio=2020, descripcion='Prueba', medio=Medio.CD)
    c = Cancion(titulo='Prueba', minutos=1, segundos=30, interprete='Juan')
    
    # u.albumes.append(a) 
    # a.canciones.append(c)
    
    # db.session.add(u)
    db.session.add(c)
    db.session.commit()
    
    # print(Album.query.all())
    # print(Album.query.all()[0].canciones)
    # print(Cancion.query.all())
    
    # db.session.delete(a)
    # print(Album.query.all())
    # print(Cancion.query.all())
    
    # album_schema = AlbumSchema()
    # cancion_schema = CancionSchema()
    # usuario_schema = UsuarioSchema()
    
    # print(Album.query.all())
    
    # print([album_schema.dumps(album) for album in Album.query.all()])
    # print([cancion_schema.dumps(cancion) for cancion in Cancion.query.all()])
    # print([usuario_schema.dumps(usuario) for usuario in Usuario.query.all()])