
.PHONY: run
run: venv
	. venv/bin/activate; python3 runserver.py

venv:
	pyvenv venv
	. venv/bin/activate; pip3 install -r requirements.txt

clean:
	rm -Rf venv/

