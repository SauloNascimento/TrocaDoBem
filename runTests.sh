#!/usr/bin/bash
./manage.py makemigrations
./manage.py migrate
./manage.py violations

function finally {
    result=1
    resultTests=$1
    if [ $resultTests = 1 ]; then
        exit $result;
    fi
}

result=0;
if [ "${CI_BUILD_REF_NAME}" = "tests" ]; then
    coverage run --source=trocadobem ./manage.py test app.tests || result=1
    finally $result
else
    coverage run --source=trocadobem ./manage.py test app.tests  --failfast || result=1

    finally $result
fi

exit $result
