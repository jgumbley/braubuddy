
venv:
	pyvenv venv
	. venv/bin/activate; pip3 install -r requirements.txt

.PHONY: run
run: venv
	. venv/bin/activate; python3 setup.py install

clean:
	rm -Rf venv/

