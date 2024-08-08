from Web_driver import WebDriver 
from Scrapper import Scrapper

# No cambiar nombre de la función
def execute_scrapping():

    chrome = WebDriver()
    chrome.initialize_driver()

    chrome.load_page("https://www.wikidex.net/")

    scrapper = Scrapper(chrome)

    pokemon_list = [
        "Pikachu", "Charizard", "Snorlax", "Gyarados", "Lugia", 
        "Eevee", "Rowlet", "Greninja", "Lucario", "Crobat", 
        "Kingambit", "Salandit", "Entei"
    ]

    pokemon_info = scrapper.extract_pokemon_info(pokemon_list)

    sorted_pokemon_info = scrapper.sort_by_weight(pokemon_info)

    scrapper.write_csv(sorted_pokemon_info)

    chrome.quit_driver()


    print("Fin del programa")

if __name__ == '__main__':
    execute_scrapping()