#!/usr/bin/env bash

echo "Run tests"

function main() {
  cd JsonToExcelParser
  export PYTHONPATH=$(pwd)

  pytest test/test.py

  test_status=$?

  if [ $test_status -eq 0 ]
  then
        cd ..
  else
        cd ..
  fi
}
main
