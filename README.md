README
====

Generate layered sphinx document.

<!-- ## Description -->

## Requirement
- python3 (confirmed: v3.6.8)

## Install

"""sh
# (optional) make python virtual enviromnent
python3 -m venv venv
# to start@bash: "source venv/bin/activate"
# to start@csh: "source venv/bin/activate.csh"
# to close: "deactivate"

pip3 install sphinx commonmark recommonmark sphinx-markdown-tables sphinx_rtd_theme

"""

## Usage

1. Edit "settings.json"
1. "generate_project.py"
1. Prepare your documents in "doc_souces". Some sample docs included initially.
1. "make_html.py"

- Autobuild  
    Execute "build_watchdog.py" and keep it running.  
    There are many other better ways. Please select what you like.

## Tips

To copy (or move) the venv, copy it and repeate "python -m venv venv".
Then the copied packages will be available.

## Licence

[MIT](https://github.com/shka86/foo/blob/master/LICENCE)

## Author

[shka86](https://github.com/shka86)
