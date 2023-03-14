MAKEFLAGS += --silent

run:
	pipenv run python src/templatopia/cli.py

acceptancetest:
	pipenv run python src/templatopia/cli.py --template template.svg --from-csv "in/list.csv" --to-path out --name-template "{{firstName}}-{{lastName}}.svg" --template-path template/ --map first_name:firstName --map last_name:lastName --common-value "date:23 Feb 2023"
	pipenv run python src/templatopia/cli.py --template test.eml --from-csv "in/list.csv" --to-path out --name-template "{{firstName}}-{{lastName}}.eml" --template-path template --map "first_name:firstName" --map "last_name:lastName" --common-value "achievement:First Python Program" --common-value "period:23-26 Feb 2023" --common-value "senderName:JD"

experiment:
	pipenv run python src/templatopia/cli.py --template template.svg --from-csv "in/list.csv" --to-path out --name-template "{{firstName}}-{{lastName}}.svg" --template-path template/ --map first_name:firstName --map last_name:lastName --map user_email:emailAddress --common-value "date:23 Feb 2023" --common-value "fromEmail: me@me.com" --common-value "signature: Me" --commonValue "emailSubject: Your Test Email" --template-2 email.eml


unittest:
	pipenv run pytest tests/unit/

test: unittest acceptancetest
