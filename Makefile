run:
	pipenv run python src/templatopia/cli.py

acceptancetest:
	pipenv run python src/templatopia/cli.py --template template.svg --from-csv "in/list.csv" --to-path out --name-template "{{firstName}}-{{lastName}}.svg" --template-path template/ --map first_name:firstName --map last_name:lastName 

unittest:
	pipenv run pytest tests/unit/

test: unittest acceptancetest
