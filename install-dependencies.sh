#!/bin/bash

pipx install poetry
poetry completions bash >> ~/.bash_completion

pipx install ruff