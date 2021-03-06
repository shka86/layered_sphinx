# -- Path setup --------------------------------------------------------------
# enable to use markdown
import sphinx_rtd_theme
from recommonmark.parser import CommonMarkParser

# enable reST extension on markdown source
from recommonmark.transform import AutoStructify


def setup(app):
    app.add_config_value('recommonmark_config', {
        'enable_auto_toc_tree': False,
    }, 'env')
    app.add_transform(AutoStructify)


# enable rtd theme

# -- Project information -----------------------------------------------------
project = 'test_prj'
copyright = '2020, author_name'
author = 'author_name'
version = '1.0'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx_markdown_tables', 'recommonmark',
]

templates_path = ['_templates']

language = 'ja'

exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
source_parsers = {
    '.md': CommonMarkParser,
}

# -- Options for HTML output -------------------------------------------------
# html_theme = "bizstyle"
html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_style = "css/my_theme.css"

html_static_path = ['_static']

master_doc = "top/index"
