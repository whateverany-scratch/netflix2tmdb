.DEFAULT_GOAL: all
.PHONY: \
 all \
 clean \
 conv \
 test

.ONESHELL:
.EXPORT_ALL_VARIABLES:
SHELL := /bin/bash
.SHELLFLAGS: -x

CONV_ARGS ?= netflix.csv tmdb.csv
ENV_FILE ?= .env
#$(shell source $(ENV_FILE))
-include $(ENV_FILE)

all: conv

clean:
	rm -f *.csv

conv:
	netflix2tmdb.py $(CONV_ARGS)

test:
	@echo "INFO: testing"

