#!/bin/sh

echo "Comparing changes between ${CI_BUILD_REF_NAME} and master";
hasCoverageData=false
for file in `git diff --name-status origin/${CI_BUILD_REF_NAME} $(git merge-base origin/master origin/${CI_BUILD_REF_NAME}) | grep "[MD]"`; do
	module=`echo $file | cut -d"/" -f5`;
	if [ "${module}" = 'parallel' ] || [ "${module}" = 'sequential' ]; then
	    feature=`echo $file | cut -d"/" -f6`;
	    if [ "${feature}" != '__init__' ]; then
            testFile=`echo $file | cut -d"/" -f8 | cut -d"." -f1`;
            if [ "${testFile}" != '' ] && [ "${testFile}" != '__init__' ]; then
                coverage run --source=trocadobem ./manage.py test app.tests.selenium_tests.${module}.${testFile} --failfast
                if [ $? != 0 ]; then
                    exit 1;
                fi
                hasCoverageData=true
            fi
        fi
	fi
done
if $hasCoverageData ; then
    coverage report
fi
