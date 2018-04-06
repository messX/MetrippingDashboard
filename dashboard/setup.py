from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar'
]

setup(name='visa',
      install_requires=requires,
      entry_points="""\
        [paste.app_factory]
        main = dashboard:main
        """,
      )
