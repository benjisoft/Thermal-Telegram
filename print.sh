#!/usr/bin/env bash
PRINTING=${1?Error: no name given}

echo $PRINTING >> printing.txt
lp -d "Star_SP512__STR_001_" printing.txt
rm printing.txt
