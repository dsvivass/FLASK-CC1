from flaskr import create_app
from .models import db, Cancion, Album, Medio, Usuario
from .models import AlbumSchema

app = create_app('default')

# Context is a dictionary that is used to store application-specific data.

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#Prueba
with app.app_context():
    # u = Usuario(nombre='Juan', contrasena='12345')
    # a = Album(titulo='Prueba', anio=2020, descripcion='Prueba', medio=Medio.CD)
    # c = Cancion(titulo='Prueba', minutos=1, segundos=30, interprete='Juan')
    
    # u.albumes.append(a) 
    # a.canciones.append(c)
    
    # db.session.add(u)
    # db.session.add(c)
    # db.session.commit()
    
    # print(Album.query.all())
    # print(Album.query.all()[0].canciones)
    # print(Cancion.query.all())
    
    # db.session.delete(a)
    # print(Album.query.all())
    # print(Cancion.query.all())
    
    album_schema = AlbumSchema()
    a = Album(titulo='Prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    db.session.add(a)
    db.session.commit()
    
    print(Album.query.all())
    
    print([album_schema.dumps(album) for album in Album.query.all()])