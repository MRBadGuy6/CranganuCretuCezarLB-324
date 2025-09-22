# LB 324

## Aufgabe 2
Erklären Sie hier, wie man `pre-commit` installiert.

Für dieses Projekt verwendet `pre-commit` (https://pre-commit.com/), um den Code automatisch zu formatieren und auch Tests ausuführen
Beim Commit wird der Code automatisch mit "black" formatiert
Beim Push werden automatisch die Tests mit pytest ausgeführt

1. Mit Rechtsklick im Ordner Powershell öffnen.
2. Pakete installieren:
- pip install -r requirements.txt
- pip install pre-commit black pytest
3. pre-commit Hooks installieren:
- pre-commit install
- pre-commit install --hook-type pre-push

Mithilfe von Python habe ich den direkten Path von meiner pre-commit.exe angegeben

## Aufgabe 4
Erklären Sie hier, wie Sie das Passwort aus Ihrer lokalen `.env` auf Azure übertragen.

tagebbbuch-a4cmecg0d5hnhhbv.switzerlandnorth-01.azurewebsites.net
