Instalacja:
Program wymaga do działania zainstalowanego środowiska Python.
Dodatkowo wymagane jest zainstalowanie pakietów pygame i pygame_gui jeśli chce się korzystać z graficznego interfejsu.
Przykład wywołania:
# pip install pygame pygame_gui

Obsługa:
 -- Skrypt main.py rozwiązuje zadanie dostarczone jako plik i zwraca rezultat jako plik.
Przykład wywołania:
# python main.py --input zadanie.txt --output rozwiazanie.txt

 -- Skrytp gui.py uruchamia edytor graficzny pozwalający na:
* losowanie zadania
* zapis i odczyt z pliku
* edycje, dodawanie i usuwanie punktów
Przykład wywołania:
# python gui.py

 -- Skrytp example_generator.py generuje przykładowe zadanie
Przykład wywołania:
# python example_generator.py 30 example_size_30.txt