from django.test import SimpleTestCase
from django.urls import reverse

class PruebasPaginaDeInicio(SimpleTestCase):
    def test_la_url_existe_en_la_ubicacion_correcta(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse('pagina de inicio'))
        self.assertEqual(respuesta.status_code, 200)

    def test_nombre_correcto_de_la_plantilla(self):
        respuesta = self.client.get(reverse("pagina de inicio"))
        self.assertTemplateUsed(respuesta, "frontend.html")

    def test_contenido_de_la_plantilla(self):
        respuesta = self.client.get(reverse("pagina de inicio"))
        self.assertContains(respuesta, "<h1>Página de inicio</h1>")
        
class PruebasPaginaDeAbout(SimpleTestCase):
    def test_la_url_existe_en_la_ubicacion_correcta(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse('pagina de inicio'))
        self.assertEqual(respuesta.status_code, 200)

    def test_nombre_correcto_de_la_plantilla(self):
        respuesta = self.client.get(reverse("pagina de inicio"))
        self.assertTemplateUsed(respuesta, "about.html")

    def test_contenido_de_la_plantilla(self):
        respuesta = self.client.get(reverse("pagina de inicio"))
        self.assertContains(respuesta, "<h1>Página de inicio</h1>")
