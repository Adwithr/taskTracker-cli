from setuptools import setup

setup(
    name="task-cli",
    version="0.1.0",
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "task-cli=main:main",
        ],
    },
)
