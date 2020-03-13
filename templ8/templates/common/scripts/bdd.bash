#!/bin/bash

# compgen to handle cases with no matches
matching_files=$(compgen -G "$(pwd)/*.feature")

for file in $matching_files; do
  output_path=$(echo "$file" | sed -E "s|$(pwd)/(..*)\.feature|$(pwd)/test_\1.py|g")
  pytest-bdd generate "$file" > "$output_path"
done
