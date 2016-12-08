import os
current_path = os.getcwd()
def tree(current_path):
        L=[]       
        content = os.listdir(current_path)
        for each in content:
                if os.path.isdir(each) and each[0]!= '.':
                        L.append(tree(current_path+os.sep+each))
                else:
                        L.append(each) 
        return L
print(tree(current_path))
