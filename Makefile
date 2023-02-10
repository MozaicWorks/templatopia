run:
	pipenv run python templatopia/cli.py

test:
	pipenv run python templatopia/cli.py --template template.svg --from-csv "in/list.csv" --to-path out --name-template "{{firstName}}-{{lastName}}.svg" --template-path template/ --map first_name:firstName --map last_name:lastName --map user_email:emailAddress
	pipenv run pytest tests/unit/
