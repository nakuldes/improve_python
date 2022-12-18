from datetime import date
class Project:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

class Task:
    def __init__(self, name, duration):
        self.name =name 
        self.duration = duration
        self.resources = []
    
    def add_resource(self, resource):
        self.resources.append(resource)

class Resources:
    def __init__(self, name, skill):
        self.name = name 
        self.skill = skill


reso_obj = Resources('Nakul', 'Python')

task_obj = Task('Initiate', 15)

task_obj.add_resource(reso_obj)

proj_obj = Project('Automate', date(2020, 1, 15), date(2021, 1, 1))

proj_obj.add_task(task_obj)

for eachtask in proj_obj.tasks:
    print(eachtask.name)
    for eachreso in eachtask.resources:
        print(eachreso.name)
        print(eachreso.skill)



