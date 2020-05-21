README
====

Generate layered sphinx document.

<!-- ## Description -->

## Requirement
- python3.6.8 on ubuntu20.04LTS, centOS6/7
- python3.7.4 on windows10

## Install

- linux

    ```sh
    # (optional) make python virtual enviromnent
    python3 -m venv venv
    # to start@bash: "source venv/bin/activate"
    # to start@csh: "source venv/bin/activate.csh"
    # to close: "deactivate"

    pip3 install sphinx commonmark recommonmark sphinx-markdown-tables sphinx_rtd_theme

    ```

- windows

    ```
    # (optional) make python virtual enviromnent
    python.exe -m venv venv
    # to start: .\venv\Scripts\activate 
    # to close: "deactivate"

    # Then the prompt will turn into (venv).

    python -m pip install --upgrade pip
    python -m pip install sphinx commonmark recommonmark sphinx-markdown-tables sphinx_rtd_theme

    ```

    - If you failed due to...
        - ExecutionPolicy, please try to change it like below.  
            ```
            > Get-ExecutionPolicy
            # maybe "Restricted" returns
            > Try Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
            ```

        - Proxy, please input proxy information as follows.
            ```
            > $env:http_proxy="username@proxy_server:port"
            > $env:https_proxy="username@proxy_server:port"
            ```

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
