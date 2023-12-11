PYFLAGS = --onefile

all: arc2 clean

arc2: arc.py
	@echo "+-------------------+"
	@echo "|   Building ARC2   |"
	@echo "+-------------------+"
	pyinstaller $(PYFLAGS) arc.py
	@echo "+-------------------+"
	@echo "|    Moving ARC2    |"
	@echo "+-------------------+"
	@mv dist/arc ~/.bin/arc

clean:
	@echo "+-------------------+"
	@echo "|  Cleaning folder  |"
	@echo "+-------------------+"
	@rm -r build
	@rm -r dist
	@rm -r arc.spec
	@echo "+-------------------+"
	@echo "|        DONE       |"
	@echo "+-------------------+"

