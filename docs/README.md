
# Dies ist die Zusammenfassung aller relevanten Dokumentationen und deren How-To-Guides.

## 1. Installation

### Installation von Python

Bevor man den KI-Chatbot verwenden kann, muss man erstmal alle relevanten externen Bibliotheken und APIs downloaden und installieren,
Dazu muss man sicherstellen, dass man [Python](https://www.python.org/downloads/) heruntergeladen und installiert hat.
Dazu folgt man diesem Link, downloadet die neueste Python-Version und folgt den Anweisungen des Installers.

Alternativ kann man unter **Windows** den **Microsoft Store** verwenden, unter **Mac** 

```zsh
brew install python
```

für **Homebrew**, oder für **Linux** je nach Distribution:

#### **Ubuntu/Debian**

```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### **Fedora**

```bash
sudo dnf install python3 python3-pip
```

#### **Arch**
    
```bash
sudo pacman -S python python-pip.
```

Falls man **Homebrew** nicht bereits installiert hat, kann man es ganz einfach in seinem Terminal mit folgendem Befehl installieren:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Installation der externen Bibliotheken

Vorausgesetzt, man befinde sich schon in einem **Terminal**, fahre man hier fort, ansonsten springe man [hier hin](#öffnen-und-bedienen-des-terminals-oder-konsole-beziehungsweise-eingabeaufforderung-unter-windows)

#### Installation von Flask, der OpenAI API etc.

Nun geht man auf das Überverzeichnis, und dort findet man eine Datei namens ***requirements.txt***. Dort stehen alle Abhängigkeiten von dem KI-Chatbot.
Diese kann man installieren, indem man zu einer virtuellen Umgebung wechselt. Deren Befehle findet man unter [venv](../venv/bin/).

Dann gibt man 

```bash
venv/bin/pip3 install -r requirements.txt
```

ein und die Abhängigkeiten werden automatisch installiert,

#### Öffnen und bedienen des Terminals (oder *Konsole* beziehungsweise *Eingabeaufforderung* unter Windows)

Unter **Windows** drückt man die *Windows-Taste* und *R* gleichzeitig und gibt dort **cmd** ein oder gibt in der *Suchleiste* **cmd** ein.
Ähnlich bei **Mac**, dort geht man auch zur Suchleiste, nur gibt man dort dann **Terminal** ein.

### Aufsetzen der Umgebung

Nachdem man alles Notwendige installiert hat, muss man noch den OpenAI-API-Schlüssel als Umgebungsvariable hinzufügen, damit

```python
client = OpenAI()
```

überhaupt Authorisierung zur Verwendung der API erhält.
Dazu findet im Überverzeichnis eine versteckte (mit einem "." davor) verschlüsselte und mit einem Passwort gesicherte Textdatei, 
welche einen validen Schlüssel beinhaltet (Passwort zur Datei und wie man die Datei entschlüsselt erfolgt auf Anfrage).


## Starten des Chatbots

Nun startet man den [Chatbot](../app/chatbot.py), indem man den Befehl 

```bash
../venv/bin/python3 chatbot.py
```
im [app](../app/)-Ordner ausführt. Wenn alles glückt, startet sich ein Server und man kann entweder unter **localhost::5000** bzw.
**127.0.0.1:5000** oder unter der untersten IP-Adresse mitsamt Port (Zahl hinter dem Doppelpunkt) den Chatbot und die Web-App starten.

Dort kann man dann mit dem Chatbot über alles Mögliche schreiben und er antwortet entsprechend.

