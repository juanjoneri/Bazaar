#!/bin/bash
export TOP=$(pwd)
cd $TOP/riscv-tools
export RISCV=$TOP/riscv
export PATH=$PATH:$RISCV/bin
cd ..
echo "all set up!"
