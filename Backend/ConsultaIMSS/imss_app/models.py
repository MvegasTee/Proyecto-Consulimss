from django.db import models

# Create your models here.

# Modelo Departamento
class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_departamento


# Modelo Equipo
class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre_equipo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    fecha_adquisicion = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre_equipo


# Modelo AplicacionEquipo
class AplicacionEquipo(models.Model):
    id_aplicacion = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    aplicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.aplicacion


# Modelo AsignacionEquipo
class AsignacionEquipo(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()
    ubicacion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Asignación {self.id_asignacion} - {self.id_equipo}"


# Modelo CaracteristicaEquipo
class CaracteristicaEquipo(models.Model):
    id_caracteristica = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    nombre_caracteristica = models.CharField(max_length=150)
    valor_caracteristica = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_caracteristica


# Modelo Fabricante
class Fabricante(models.Model):
    id_fabricante = models.AutoField(primary_key=True)
    nombre_fabricante = models.CharField(max_length=150)
    pais = models.CharField(max_length=100, blank=True, null=True)
    sitio_web = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_fabricante


# Modelo HistorialEquipo
class HistorialEquipo(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_evento = models.DateField()
    tipo_evento = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Historial {self.id_historial} - {self.id_equipo}"


# Modelo Mantenimiento
class Mantenimiento(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_mantenimiento = models.DateField()
    tipo_mantenimiento = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    responsable = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"Mantenimiento {self.id_mantenimiento} - {self.id_equipo}"


# Modelo Proveedor
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=150)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    sitio_web = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_proveedor


# Modelo EquipoProveedor
class EquipoProveedor(models.Model):
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_compra = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ('id_equipo', 'id_proveedor')

    def __str__(self):
        return f"Equipo: {self.id_equipo} - Proveedor: {self.id_proveedor}"


# Modelo Usuario
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre_usuario


# Modelo Historial de Búsquedas
class HistorialBusqueda(models.Model):
    id_historial = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    termino_busqueda = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Búsqueda {self.id_historial} - {self.usuario}"
