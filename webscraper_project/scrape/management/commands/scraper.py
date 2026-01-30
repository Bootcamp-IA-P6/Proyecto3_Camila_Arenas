from django.core.management.base import BaseCommand
from scrape.services.scrape import scrape_website
from scrape.models import ScrapedData

class Command(BaseCommand):
    help = "Run the web scraper"
    # Hereda de BaseCommand, lo que permite que este comando sea ejecutable mediante python manage.py <nombre_comando>.

    def handle(self, *args, **options):
        scraped_data = scrape_website()  # Aquí obtienes la lista con 'author' y 'quote'
        
        for item in scraped_data:
            # CAMBIA ESTA LÍNEA:
            ScrapedData.objects.create(
                author=item["author"],  
                quote=item["quote"]     
            )
            
        self.stdout.write(self.style.SUCCESS('¡Datos guardados exitosamente en la DB!'))
