import sys,os
path=os.getcwd()
path=path.split('automation_framework_demo',1)[0]
path=path+'automation_framework_demo'
# print(path)
sys.path.append(path)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)