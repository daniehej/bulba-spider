# bulba-spider

A web crawler which gathers Pokémon name translations for the purpose of generating a Chinese-English Pokémon dictionary.

Data is obtained from Bulbapedia, namely the list of Chinese Pokémon names (https://bulbapedia.bulbagarden.net/wiki/List_of_Chinese_Pokémon_names), and the explanations of the names are obtained from each creature's individual page (https://bulbapedia.bulbagarden.net/wiki/{x}_(Pok%C3%A9mon)). 

The parsed results of the crawler can be found in the file `cn-pkmn.txt` and contain information from Bulbapedia which is available under an Attribution-NonCommercial-ShareAlike 2.5 license (CC BY-NC-SA 2.5).
Other files in the repository are available under the MIT License.

## Dependencies
```
scrapy
```

## Usage
A list of English Pokémon names to crawl is given in `pkm-names.txt`.

A list of Items to crawl is given in `item-names.txt`.

For a dictionary of Pokémon names, run
```
scrapy runspider main.py
python json-parse.py
```

For a dictionary of Items, use

```
scrapy runspider item.py
python json-parse.py
```
