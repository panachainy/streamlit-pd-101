SHELL := /bin/zsh

p: prepair
prepair:
	npm i -g nodemon

i:
	poetry install

sh:
	poetry shell

d: dev
dev:
	python -m streamlit run src/main.py 
