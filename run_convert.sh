#!/usr/bin/env bash

echo "CONVERT JSON TO SPREADSHEETS"

function main() {

  if [ ! -d tables ]
    then
      mkdir -p tables
    fi
  python JsonToExcelParser/main.py --input_path=test/wekan.json --output_path=tables/
  cd ..
}

main
