import re
import time
import streamlit as st


password_rules = {
    "upper case": 1,
    "lower case": 1,
    "minimum length": 9,
    "maximum length": 16,
    "special characters": 1,
    "allowed special characters": [".", ",", "(", ")", "-", "_", "*", "@", "/","\\"]
}

def isValidPassword(input_pw, rules=dict):
    if rules is None:
        rules = password_rules
    return True



class EmailInput:
    def __init__(self, email):
        self.email = email

class PasswordInput:
    def __init__(self, password):
        self.password = password
