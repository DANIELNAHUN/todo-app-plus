from sqlalchemy import Column, ForeignKey, Text
from sqlalchemy.sql.sqltypes import DateTime, Integer, String

from config.db_todo import Base


class Empresas(Base):
  __tablename__ = 'empresas'
  id_empresa = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Ciudades(Base):
  __tablename__ = 'ciudades'
  id_ciudad = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Oficinas(Base):
  __tablename__ = 'oficinas'
  id_oficina = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  ubicacion = Column(Text)
  id_ciudad = Column(Integer, ForeignKey('ciudades.id_ciudad'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class EmpresasCiudades(Base):
  __tablename__ = 'empresas_ciudades'
  id_empresa_ciudad = Column(Integer, primary_key=True, autoincrement=True)
  id_empresa = Column(Integer, ForeignKey('empresas.id_empresa'))
  id_ciudad = Column(Integer, ForeignKey('ciudades.id_ciudad'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Areas(Base):
  __tablename__ = 'areas'
  id_area = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Cargos(Base):
  __tablename__ = 'cargos'
  id_cargo = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  id_area = Column(Integer, ForeignKey('areas.id_area'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Equipos(Base):
  __tablename__ = 'equipos'
  id_equipo = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Roles(Base):
  __tablename__ = 'roles'
  id_rol = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class TagPermisos(Base):
  __tablename__ = 'tag_permisos'
  id_tag = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Permisos(Base):
  __tablename__ = 'permisos'
  id_permiso = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  id_tag = Column(Integer, ForeignKey('tag_permisos.id_tag'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class RolesPermisos(Base):
  __tablename__ = 'roles_permisos'
  id_rol_permiso = Column(Integer, primary_key=True, autoincrement=True)
  id_rol = Column(Integer, ForeignKey('roles.id_rol'))
  id_permiso = Column(Integer, ForeignKey('permisos.id_permiso'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class UsuariosRoles(Base):
  __tablename__ = 'usuarios_roles'
  id_usuario_rol = Column(Integer, primary_key=True, autoincrement=True)
  id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
  id_rol = Column(Integer, ForeignKey('roles.id_rol'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class UsuariosPermisos(Base):
  __tablename__ = 'usuarios_permisos'
  id_usuario_permiso = Column(Integer, primary_key=True, autoincrement=True)
  id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
  id_permiso = Column(Integer, ForeignKey('permisos.id_permiso'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Logs(Base):
  __tablename__ = 'logs'
  id_log = Column(Integer, primary_key=True, autoincrement=True)
  id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
  accion = Column(String(250))
  tabla = Column(String(250))
  campo = Column(String(250))
  valor_anterior = Column(Text)
  valor_nuevo = Column(Text)
  descripcion = Column(Text)
  fecha_creacion = Column(DateTime)