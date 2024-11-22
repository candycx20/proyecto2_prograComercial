from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Categoria, Proveedor
import unittest
from .views import *

class CategoriaTest(TestCase):
    def setUp(self):
        self.cat = CategoriaListCreate()
        
        # Crear un usuario de prueba y autenticarse
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')  # Autenticar al usuario
        
        # Crear una categoría de ejemplo
        self.categoria = Categoria.objects.create(nombre="Test Categoria", descripcion="Descripción de prueba")
        
        # Definir URLs para la categoría
        self.url_list_create = reverse('categoria-list-create')
        self.url_detail = reverse('categoria-detail', args=[self.categoria.id])

    # def test_create_categoria(self):
    #     """Prueba para crear una nueva categoría"""
    #     data = {"nombre": "Nueva Categoria", "descripcion": "Nueva descripción"}
    #     response = self.client.post(self.url_list_create, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.data["nombre"], "Nueva Categoria")

    def test_read_categoria(self):
        """Prueba para leer una categoría existente"""
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nombre"], self.categoria.nombre)

    # def test_update_categoria(self):
    #     """Prueba para actualizar una categoría existente"""
    #     data = {"nombre": "Categoria Actualizada", "descripcion": "Descripción actualizada"}
    #     response = self.client.put(self.url_detail, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data["nombre"], "Categoria Actualizada")

    # def test_delete_categoria(self):
    #     """Prueba para eliminar una categoría existente"""
    #     response = self.client.delete(self.url_detail)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertFalse(Categoria.objects.filter(id=self.categoria.id).exists())


