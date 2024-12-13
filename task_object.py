class Task:
    def __init__(self, description, day):
        
        self.description = description
        self.day = day

    def __str__(self):
         return f"Task: {self.description}, Day: {self.day}"


