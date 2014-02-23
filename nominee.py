class Nominee(object):
    def __init__(self, name):
        self.name = name
        
    def short_name(self, fdist):
        """The most useful portion of this name"""
        return self.name
