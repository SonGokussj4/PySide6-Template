
venvName = venv
pyside6-uic = ${venvName}/Scripts/pyside6-uic.exe
pyside6-rcc = ${venvName}/Scripts/pyside6-rcc.exe

ui:
# WINDOWS
ifeq ($(OS),Windows_NT)
	${pyside6-uic} .\mainWindow.ui -o .\src\ui\mainWindow.py
# ${pyside6-rcc} .\app.qrc -o .\src\ui\resources\app_rc.py

# ${pyside6-uic} .\designer\about.ui -o .\src\ui\about.py
# ${pyside6-rcc} .\designer\about.qrc -o .\src\ui\resources\about_rc.py

# ${pyside6-uic} .\designer\settings.ui -o .\src\ui\settings.py
# LINUX
else
	find designer/ -iname "*.ui" -exec basename {} .ui \; | xargs -I {} pyside6-uic designer/{}.ui -o src/ui/{}.py
	find designer/ -iname "*.qrc" -exec basename {} .qrc \; | xargs -I {} pyside6-rcc designer/{}.qrc -o src/ui/resources/{}_rc.py
endif

run:
	python main.py

build:
	pyinstaller --onefile --windowed main.py
