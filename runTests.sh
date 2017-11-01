#!/usr/bin/bash

function finally {
    sh killPhantom.sh || result=1
    resultTests=$1
    if [ $resultTests = 1 ]; then
#        . releaseServerDeploy.sh
        exit $result;
    fi
}

result=0;
if [ "${CI_BUILD_REF_NAME}" = "tests" ]; then

    for test in `find app/tests/selenium_tests/parallel/ -type f -name "*adm*"`; do
        #test_name=`echo $test | cut -d"/" -f8 | cut -d"." -f1`;
        cp $test $admin_folder;
    done
    coverage run --source=trocadobem ./manage.py test app.tests.selenium_tests|| result=1
    finally $result

else
#    coverage run --source=trocadobem ./manage.py test app.tests.selenium_tests.sequential.login --failfast || result=1
#
#    finally $result
#
#    coverage run --source=trocadobem ./manage.py test app.tests.selenium_tests.parallel.login --failfast || result=1
    coverage run --source=trocadobem ./manage.py test app.tests.selenium_tests --failfast || result=1
    finally $result
fi

sh runChangedTests.sh || result=1
sh killPhantom.sh || result=1
#. releaseServerDeploy.sh || result=1

exit $result
