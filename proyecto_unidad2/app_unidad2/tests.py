from django.test import TestCase
from .models import Autor, Editorial, Libro
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(
            nombre="Gabriel",
            apellido="García Márquez",
            nacionalidad="Colombiana",
            fecha_nacimiento="1927-03-06"
        )
        
        self.editorial = Editorial.objects.create(
            nombre="Editorial Sudamericana",
            direccion="Av. Corrientes 123, Buenos Aires",
            pais="Argentina"
        )
        
        self.libro = Libro.objects.create(
            titulo="Cien años de soledad",
            fecha_publicacion="1967-05-30",
            numero_paginas=471,
            autor=self.autor,
            editorial=self.editorial
        )

    def test_autor_creacion(self):
        self.assertEqual(self.autor.nombre, "Gabriel")
        self.assertEqual(self.autor.apellido, "García Márquez")
        
    def test_editorial_creacion(self):
        self.assertEqual(self.editorial.nombre, "Editorial Sudamericana")
        
    def test_libro_creacion(self):
        self.assertEqual(self.libro.titulo, "Cien años de soledad")
        self.assertEqual(self.libro.autor, self.autor)