class Course:
    def __init__(self, name, code, credithour):
        self.name = name
        self.code = code
        self.credithour = credithour
    
    def get_details(self):
        return f"Course: {self.name}, code: {self.code}, credithour: {self.credithour}"

class WebDevClass(Course):
    def __init__(self, name, code, credithour):
        super().__init__(name, code, credithour)
    
    def get_details(self):
        return f"Web Development Course: {self.name}, code: {self.code}, credithour: {self.credithour}"


course1 = Course("global-trend", "gt101", 2)
web_dev_course = WebDevClass("html", "ht101",3 )

print(course1.get_details())
print(web_dev_course.get_details())
