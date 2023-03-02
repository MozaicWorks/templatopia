MAKEFLAGS += --silent

run:
	pipenv run python src/templatopia/cli.py

acceptancetest:
	pipenv run python src/templatopia/cli.py --template template.svg --from-csv "in/list.csv" --to-path out --name-template "{{firstName}}-{{lastName}}.svg" --template-path template/ --map first_name:firstName --map last_name:lastName --common-value "date:23 Feb 2023"

unittest:
	pipenv run pytest tests/unit/

test: unittest acceptancetest
