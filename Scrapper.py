from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Web_driver import WebDriver 
import csv
import os
from selenium.common.exceptions import NoSuchElementException

class Scrapper:

    # No modificar
    def __init__(self, chrome: WebDriver):
        self.chrome = chrome

    def find_pokemon(self, nombre: str) -> None:
        search_box = self.chrome.find_element(By.ID, 'searchInput')
        self.chrome.write_in_element(By.ID, 'searchInput', nombre)
        self.chrome.click_element(By.ID, 'searchButton')

    def extract_pokemon_info(self, pokemon_list: list[str]) -> list:
        info_pokemons = []
        for pokemon_name in pokemon_list:
            try:
                self.find_pokemon(pokemon_name)

                data_table = self.chrome.find_element(By.CLASS_NAME, 'datos')
                rows = data_table.find_elements(By.TAG_NAME, 'tr')

                tipo_elements = rows[3].find_elements(By.TAG_NAME, 'td')

                tipo1 = ""
                tipo2 = ""

                for tipo_element in tipo_elements:
                    tipo_imgs = tipo_element.find_elements(By.TAG_NAME, 'img')
                    for img in tipo_imgs:
                        tipo = img.get_attribute('alt')
                        tipo = tipo.replace('.gif', '') 
                        tipo = tipo.replace("Tipo ", "")
                        tipo = tipo.upper() 
                        if tipo1 == "":
                            tipo1 = tipo
                        else:
                            tipo2 = tipo
                if not tipo2:
                    tipo2 = ""

                categoria = rows[2].find_element(By.TAG_NAME, 'td').text.strip() 
                categoria = categoria.upper()
                peso_text = rows[6].find_element(By.TAG_NAME, 'td').text.strip() 
                altura = rows[7].find_element(By.TAG_NAME, 'td').text.strip() 
                altura = altura.replace("m", "M")

                peso = float(peso_text.replace(' kg', '').replace(',', '.'))

                pokemon_info = [pokemon_name.upper(), tipo1, tipo2, categoria, peso, altura]
                info_pokemons.append(pokemon_info)
            except NoSuchElementException:
                print(f"No se pudo encontrar información para {pokemon_name}")

        return info_pokemons
    

 # COMPLETAR
    def sort_by_weight(self, info: list) -> list:
        filtered_info = [pokemon_info for pokemon_info in info if pokemon_info[4]]
        sorted_info = sorted(filtered_info, key=lambda x: float(x[4]), reverse=True)
        return sorted_info

    def write_csv(self, info: list) -> None:
        header = "NOMBRE;TIPO1;TIPO2;CATEGORIA;PESO;ALTURA\n"
        filename = 'pokemons.csv'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(header)
            for pokemon in info:
                peso_formateado = f"{pokemon[4]:.1f}".replace('.', ',') + " KG"
                pokemon[4] = peso_formateado
                line = ";".join(pokemon) + "\n"
                file.write(line)
        print(f"Se ha creado el archivo {filename}\n")
