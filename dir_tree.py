import os

def get_directory_tree(path,delimiter):

    print(delimiter+path)

    dir_list = os.listdir(path)

    for i in range(len(dir_list)):

        sub_dir = path+'\\'+dir_list[i]

        if os.path.isdir(sub_dir):

            get_directory_tree(sub_dir, '|' + delimiter)
        
        else:

            print(delimiter+sub_dir)



  
if __name__ == '__main__':

    path = input("Enter the directory path: ")

    get_directory_tree(path,'--')

    


