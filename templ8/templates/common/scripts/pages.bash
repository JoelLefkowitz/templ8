#!/bin/bash
src="../briefs"
briefs=$(find $src -maxdepth 1 -type f -name "*.md" ! -name "README.md")
mdmerge -o $src/README.md $briefs
