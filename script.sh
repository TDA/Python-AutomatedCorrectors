#!/usr/bin/env bash
valgrind --tool=memcheck --leak-check=yes --error-exitcode=21 $1
