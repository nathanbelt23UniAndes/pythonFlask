from  flaskr import create_app
from .modelos import  Usuario,Cancion, Album, db,Medio, AlbumSchema, UsuarioSchema


app=create_app('default')
app_context= app.app_context()
app_context.push()


db.init_app(app)
db.create_all()


#prueba
with app.app_context():
  print("entre")
  # album_schema= AlbumSchema()
  # usuario_schema=UsuarioSchema()
  # u=Usuario( nombre ="yonathan usuario", contrasena = "1234")
  # c=Cancion(titulo='la gota fria', minutos=12, segundos=10, interprete= 'prueba')
  # a=Album(titulo="demo",anio=1998, descripcion="none",medio=Medio.CASETE)
  # u.albumes.append(a)
  # db.session.add(u)
  # db.session.commit()
  
  # print('json')
  # print({album_schema.dumps(album) for album in Album.query.all()})
  # print({usuario_schema.dumps(album) for album in Usuario.query.all()})

