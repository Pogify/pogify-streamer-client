py = python3
cc := ${py} -m PyInstaller


all: init build

.PHONY: build

init:
	$(py) -m pip install pyinstaller requests

build:
	$(cc) launch.spec

clean:
	rm -rf dist/ build/

