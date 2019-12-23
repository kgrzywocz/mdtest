#!/bin/bash
set -e
PATH=../../bin:$PATH
PYTHONPATH=../..
cd mdtest/tests


function fail {
	echo '	fail'
	echo "Detailed output:"
	echo "$1"
	exit -1
}


for TEST_SUTE in `ls mdtest_tests/*.md`
do
	echo -n '	runnig:' $TEST_SUTE
	set +e
		OUTPUT=`mdtest $TEST_SUTE 2>&1`
		EXIT_CODE=$?
	set -e
	echo "$OUTPUT" | python3 $TEST_SUTE.py $EXIT_CODE || fail "$OUTPUT"
	echo '	pass'
done

echo PASSED