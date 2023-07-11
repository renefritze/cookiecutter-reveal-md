
static_html/index.html: slides/{{cookiecutter.file_name}}.md slides/qr_self.png
	npm run html

slides/{{cookiecutter.file_name}}.pdf: static_html/index.html
	npm run pdf

install:
	npm install

html: static_html/index.html

pdf: slides/{{cookiecutter.file_name}}.pdf

watch:
	npm run watch

ifeq ($(OS),Windows_NT)
    VENV_ACTIVATE := . venv/Scripts/activate
else ifeq ($(shell uname),Linux)
    VENV_ACTIVATE := . venv/bin/activate
endif

# this way we only re-run install if requirements change
venv/setup_by_make: requirements-dev.txt
	test -d venv || python3 -m venv venv
	$(VENV_ACTIVATE) && python3 -m pip install -q -r requirements-dev.txt
	touch venv/setup_by_make

venv: venv/setup_by_make

slides/qr_%.png: venv
	$(VENV_ACTIVATE) && python render_qr.py
	mv -f qr_*png slides/

clean:
	rm -f qr_*png
	mv static_html/edit .
	rm -rf static_html/*
	mv edit static_html/
