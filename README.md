## Quick Start (Szybki start)

Aby szybko uruchomić projekt lokalnie na systemie Windows, wykonaj poniższe kroki:

**Klonowanie repozytorium**
```bash
git clone https://github.com/lesiak67/template-python-project
cd template-python-project

## Inicjalizacja środowiska wirtualnego i instalacja zależności

Uruchom przygotowany skrypt, który automatycznie utworzy folder .venv, aktywuje go i pobierze wymagane pakiety z pliku requirements.txt: scripts\init_venv.bat


Uruchom aplikację:
Po poprawnej instalacji możesz uruchomić główny program za pomocą polecenia: scripts\run.bat

##Lintowanie, formatowanie i testowanie kodu

Lintowanie
Uruchom przygotowany skrypt - scripts\lint.bat

Formatowanie
Uruchom przygotowany skrypt - scripts\code_formatting.bat

Testy jednostkowe
Uruchom przygotowany skrypt - scripts\test.bat

## CI Pipeline

Projekt wykorzystuje GitHub Actions do automatycznej weryfikacji jakości kodu. Plik konfiguracyjny (workflow) znajduje się w .github/workflows/test_workflow.yml.

Kiedy uruchamiany jest pipeline?
    Przy każdym wypchnięciu kodu (push) na główną gałąź (main).
    Przy tworzeniu żądań scalenia (pull request) do głównej gałęzi.

Co sprawdza pipeline?
Proces uruchamia się na wirtualnej maszynie z systemem Windows (windows-latest) i sekwencyjnie wykonuje następujące kroki:
    Set up: Pobranie kodu repozytorium i konfiguracja środowiska Python.
    Inicjalizacja: Utworzenie wirtualnego środowiska i instalacja zależności (init_venv.bat).
    Weryfikacja formatowania: Sprawdzenie kodu narzędziem Black (code_formatting.bat).
    Analiza statyczna (Linting): Uruchomienie Pylinta (lint.bat). Ważne: Jeśli Pylint znajdzie naruszenia standardów lub błędy, rzuci wyjątkiem i zatrzyma cały workflow (zakończy się on statusem błędu - czerwony krzyżyk).
    Testowanie: Uruchomienie testów jednostkowych (test.bat) w celu potwierdzenia, że nowe zmiany nie popsuły istniejącej funkcjonalności aplikacji. Niezaliczenie choćby jednego testu również skutkuje przerwaniem procesu CI.