"""A basic (single function) API written using Hug"""
import hug


@hug.get('/happy_birthday', examples="name=HUG&age=1")
def happy_birthday(name: hug.types.text, age: hug.types.number):
    """Says happy birthday to a user"""
    return "Happy {0} Birthday {1}!".format(name, age)