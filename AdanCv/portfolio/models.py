from django.db import models

# Create your models here.

class Proyecto(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo") # cadena de caracteres en la bdd
    description = models.TextField(default='',verbose_name="Descripción") # campo de texto
    image = models.ImageField(verbose_name="Imagen", upload_to="projects") # campo de imagen
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación") # se añade la hora automaticamente
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición") # se actualiza cuando se modifica
    

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural ="proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title