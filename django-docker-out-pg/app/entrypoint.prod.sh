#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


if [ -z "${SQL_USER}" ]; then
    base_postgres_image_default_user='postgres'
    export SQL_USER="${base_postgres_image_default_user}"
fi
# export DATABASE_URL="postgres://${SQL_USER}:${SQL_PASSWORD}@${SQL_HOST}:${SQL_PORT}/${SQL_DATABASE}"

>&2 echo 'PostgreSQL is available'

exec "$@"
