py = python3
cc := ${py} -m PyInstaller


all: build

.PHONY: build

build:
	$(cc) launch.spec

clean:
	rm -rf dist/ build/

