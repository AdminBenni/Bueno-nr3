# import os
# import sys
# import random
# import re
# import json
# from time import time as epoch
from bottle import *
# from pymysql import *

@route("/res/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./res")
@route("/res/fonts/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./res/fonts")
@route("/res/imgs/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./res/imgs")
@route("/res/style/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./res/style")

@route("/")
def home():
    return template("index")

run()