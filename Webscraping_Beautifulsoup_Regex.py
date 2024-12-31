import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from typing import List, Tuple
from pathlib import Path

class ElementosScraper:
    def __init__(self, url: str, ruta_salida: str):
        self.url = url
        self.ruta_salida = Path(ruta_salida)
        self.elementos = []
        self.datos_elementos: List[Tuple[str, int, str]] = []

    def escrapear_elementos(self) -> None:
        """Obtiene los elementos de transición de la página web."""
        try:
            respuesta = requests.get(self.url)
            respuesta.raise_for_status()  # Verifica si hay errores en la respuesta
            pagina = BeautifulSoup(respuesta.text, "html.parser")
            self.elementos = pagina.find_all(bgcolor="#81F7BE")
            
            if not self.elementos:
                raise ValueError("No se encontraron elementos en la página")
                
        except requests.RequestException as e:
            print(f"Error al obtener la página: {e}")
            raise
            
    def extraer_datos_elementos(self) -> None:
        """Extrae nombre, número atómico y símbolo de cada elemento."""
        for elemento in self.elementos[:-1]:  # Excluye el último elemento
            texto = str(elemento)
            try:
                # Extrae el título (nombre del elemento)
                title_match = re.search('title="(.*?)"', texto)
                if not title_match:
                    continue
                titulo = title_match.group(1)

                # Extrae el número atómico
                num_atomico_match = re.search('<b>(.*?)</b>', texto)
                if not num_atomico_match:
                    continue
                numero_atomico = int(num_atomico_match.group(1))

                # Extrae el símbolo
                simbolo_match = re.search('>(.*?)</a>', texto)
                if not simbolo_match:
                    continue
                simbolo = simbolo_match.group(1)

                self.datos_elementos.append((titulo, numero_atomico, simbolo))
                
            except (ValueError, AttributeError) as e:
                print(f"Error al procesar elemento: {e}")
                continue

    def guardar_csv(self) -> None:
        """Guarda los datos extraídos en un archivo CSV."""
        try:
            df = pd.DataFrame(
                self.datos_elementos, 
                columns=['Nombre', 'Numero_Atomico', 'Simbolo']
            )
            df.to_csv(self.ruta_salida, index=False)
            print(f"Datos guardados exitosamente en {self.ruta_salida}")
            
        except Exception as e:
            print(f"Error al guardar el archivo CSV: {e}")
            raise

    def ejecutar_scraping(self) -> None:
        """Ejecuta el proceso completo de scraping."""
        print("Iniciando scraping de elementos...")
        self.escrapear_elementos()
        print("Extrayendo datos de los elementos...")
        self.extraer_datos_elementos()
        print("Guardando resultados...")
        self.guardar_csv()
        print("Proceso completado.")

def main():
    url = "https://es.wikipedia.org/wiki/Tabla_peri%C3%B3dica_de_los_elementos"
    ruta_salida = "Metales_de_transicion.csv"
    
    try:
        scraper = ElementosScraper(url, ruta_salida)
        scraper.ejecutar_scraping()
    except Exception as e:
        print(f"Error en la ejecución: {e}")

if __name__ == "__main__":
    main()