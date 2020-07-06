#!/bin/bash
# Run pytest-bdd generate on all *.feature files

# Compgen to handle cases with no matches
matching_files=$(compgen -G "$(pwd)/*.feature")

for file in $matching_files; do
  output_path=$(echo "$file" | sed -E "s|$(pwd)/(..*)\.feature|$(pwd)/test_\1.py|g")
  if [ -f "$output_path" ]; then
    echo $output_path already exists
  else
    echo Generating $output_path
    pytest-bdd generate "$file" > "$output_path"
  fi
done
