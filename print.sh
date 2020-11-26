#!/usr/bin/env bash
PRINTING=${1?Error: no name given}

echo $PRINTING >> printing.txt
lp printing.txt
rm printing.txt