#!/usr/bin/env bash

echo "Convert json to xsls"

function main() {
  cd JsonToExcelParser

  if [ ! -d tables ]
    then
      mkdir -p tables
    fi
  python main.py --input_path=test/wekan.json --output_path=tables/
  cd ..
}

main
