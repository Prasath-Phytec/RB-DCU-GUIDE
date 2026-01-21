project = 'RB-DCU i.MX 6ULL'
copyright = '2025, PHYTEC'
author = 'PHYTEC'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    # 'myst_parser',  # Enable if using Markdown
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = [
    'sidebar-toggle.js',
]

html_logo = '_static/logo.png'

html_theme_options = {
    'collapse_navigation': True,
    'navigation_depth': 4,
    'style_external_links': True,
    'logo_only': False,
}

rst_prolog = """
.. role:: raw-html(raw)
   :format: html
"""

html_show_sourcelink = False

