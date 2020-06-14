Instalacja:
Program wymaga do działania zainstalowanego środowiska Python w wersji 3.x.
Do działania aplikacji z interfejsem graficznym wymagane jest doinstalowanie pakietów pygame i pygame_gui.
Przykład wywołania:
# pip install pygame pygame_gui

Obsługa:
 -- Skrypt main.py rozwiązuje zadanie problemu dostarczone jako plik i zwraca rezultat jako plik.
Przykład wywołania:
# python main.py --input zadanie.txt --output rozwiazanie.txt

 -- Skrypt example_generator.py generuje przykładowe zadanie problemu o określonej wielkości do wskazanego pliku.
Przykład wywołania:
# python example_generator.py 30 przykladowe_zadanie_30.txt

 -- Skrypt gui.py uruchamia edytor graficzny pozwalający na edycję instancji problemu oraz wizualizację wyników działania algorytmu.
Przykład wywołania:
# python gui.py
