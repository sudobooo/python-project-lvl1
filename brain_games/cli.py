import prompt
"""Simplify input and output."""


def welcome_user():
    """Return username input."""
    name = prompt.string('May I have your name? ')
    return print('Hello, {0}'.format(name))
