# Create your classes here
class Student(object):
    """docstring for Student"""
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """docstring for Question"""
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class Exame(object):
    """docstring for Exame"""
    def __init__(self, name):
        self.name = name
        self.questions = {}
        
        
        
        