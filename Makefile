MAKEFLAGS += --silent
python=pipenv run python
cli=src/templatopia/cli.py

run:
	$(python) $(cli)

acceptancetest:
	$(python) $(cli) --template template.svg --from-csv "in/list.csv" --to-path out --name-template "{{firstName}}-{{lastName}}.svg" --template-path template/ --map first_name:firstName --map last_name:lastName --common-value "date:23 Feb 2023"
	$(python) $(cli) --template template.eml --from-csv "in/list.csv" --to-path out --name-template "{{firstName}}-{{lastName}}.eml" --template-path template --map "first_name:firstName" --map "last_name:lastName" --common-value "achievement:First Python Program" --common-value "period:23-26 Feb 2023" --common-value "senderName:JD"
	$(python) $(cli) --template template.eml --from-csv "in/list.csv" --name-template "{{firstName}}-{{lastName}}-1.eml" --map "first_name:firstName" --map "last_name:lastName" --common-value "achievement:First Python Program" --common-value "period:23-26 Feb 2023" --common-value "senderName:JD"
	$(python) $(cli) --template template.eml --from-csv "in/list.csv" --name-template "{{firstName}}-{{lastName}}-2.eml"

experiment:
	$(python) $(cli) --template template.svg --from-csv "in/list.csv" --name-template "Hello-{{firstName}}-{{lastName}}.svg" --map "first_name:firstName" --map "last_name:lastName" --map "user_email:emailAddress" --common-value "date:23 Feb 2023" --common-value "fromEmail: me@me.com" --template-2 template-attach.eml


unittest:
	pipenv run pytest tests/unit/

test: unittest acceptancetest
