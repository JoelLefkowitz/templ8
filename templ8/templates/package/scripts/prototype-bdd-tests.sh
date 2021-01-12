#!/bin/bash
# Run pytest-bdd generate on all *.feature files

bdd_test_directory=$1

# Compgen to handle cases with no matches
matching_files=$(compgen -G "$bdd_test_directory/*.feature")

for file in $matching_files; do
    output_path=$(echo "$file" | sed -E "s|$bdd_test_directory/(..*)\.feature|$bdd_test_directory/test_\1.py|g")
    if [ -f "$output_path" ]; then
        echo "$output_path" already exists
    else
        echo Generating "$output_path"
        pytest-bdd generate "$file" > "$output_path"
    fi
done
