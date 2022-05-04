#!/bin/bash

if [ "$DATABASE" = "mariadb" ]
then
	echo "Waiting for mariadb to be up"

	while ! nc -z $MARIADB_HOST $MARIADB_PORT; do
	  sleep 0.2
	done

	echo "Mariadb started"
fi

echo "GRANT ALL on *.* to '${MARIADB_USER}'; "| mysql -u root --password="${MARIADB_ROOT_PASSWORD}" -h "${MARIADB_HOST}"

python westerosdictator/manage.py flush --no-input
python westerosdictator/manage.py migrate
python westerosdictator/manage.py loaddata db.json
python westerosdictator/manage.py collectstatic --noinput 

exec "$@"

