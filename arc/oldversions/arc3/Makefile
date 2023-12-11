PYFLAGS = --onefile
APPNAME = arc

install: build move clean

build: main.py
	@echo "+-------------------+"
	@echo "|   Building ARC3   |"
	@echo "+-------------------+"
	pyinstaller $(PYFLAGS) main.py

move:
	@echo "+-------------------+"
	@echo "|    Moving ARC3    |"
	@echo "+-------------------+"
	@mv dist/main ~/.bin/$(APPNAME)

clean:
	@echo "+-------------------+"
	@echo "|  Cleaning folder  |"
	@echo "+-------------------+"
	@rm -r build
	@rm -r dist
	@rm -r main.spec
	@echo "+-------------------+"
	@echo "|        DONE       |"
	@echo "+-------------------+"

edit:
	nvim -p main.py utils.py settings.py
