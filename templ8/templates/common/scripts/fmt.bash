#!/bin/bash
black . --exclude venv
prettier --single-quote --trailing-comma es5 --write "/**/*.{js, ts}"
