class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    
    def display_info(self):
        print(f"Skolotājas vārds: {self.name}")
        print(f"Priekšmets: {self.subject}")
    
    def change_subject(self, new_subject):
        self.subject = new_subject
        print(f"{self.name} tagad māca {self.subject}.")

#Create a Teacher object
teacher1 = Teacher("Alise", "Matemātika")
teacher1.display_info()

#Update the subject
teacher1.change_subject("Fizika")
teacher1.display_info()