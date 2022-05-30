import os
#Step1:GO through the parent directory

class dir:
    def __init__(self,dir,depth,file_list):
        self.dir=dir
        self.depth=depth
        self.file_list=[]

def Recurse_directory(dirname):

        global file_count, Dircount, depth
        for contents in os.listdir(dirname):
              depth=depth+1
              if(os.path.isdir(dirname+"/"+contents)):
                        Dircount=Dircount+1
                        files_list= listfiles(dirname+"/"+contents,contents)
                        depth = depth + 1
                        for files in files_list:

                            print_with_depth(depth,dir=False)
                            print(files)
              else:
                     file_count=file_count+1
                     print_with_depth(depth, dir=False,same_dir=True)
                     print(contents)


def Recurse_directory_with_Depth(dirname):
    global file_count, Dircount, depth
    for contents in os.listdir(dirname):
        if (os.path.isdir(dirname + "/" + contents)):
            newfolder=dir(dirname + "/" + contents,0,None)  #creating new instance for each directory
            Dircount = Dircount + 1
            files_list = listfiles_with_depth(newfolder)
            depth = depth + 1
            for files in files_list:
                print_with_depth(newfolder.depth, dir=False)
                print(files)
        else:
            file_count = file_count + 1
            print_with_depth(depth, dir=False, same_dir=True)
            print(contents)


def listfiles(directories,contents):
        global file_count,depth
        list_files=[]
        for child_dirs in os.listdir(directories):
                depth=depth+1
                print_with_depth(depth,dir=True)
                print(contents)
                if(os.path.isfile(directories+"/"+child_dirs)):
                    file_count=file_count+1
                    list_files.append(child_dirs)
                else:
                        print(child_dirs)
                        Recurse_directory(directories+"/"+child_dirs)

        return list_files


def listfiles_with_depth(new_directory):
    global file_count, depth
    list_files = []
    for child_dirs in os.listdir(new_directory.dir):#child_directories or files
        #if directories it will have new tree and will need to recurse again
        #if files add it to the list of files
        new_directory.depth=new_directory.depth+1
        print_with_depth(depth, dir=True,same_dir=True)
        print(new_directory.dir)
        if (os.path.isfile(new_directory.dir+"/"+child_dirs)):
            file_count = file_count + 1
            new_directory.file_list.append(child_dirs)
        else:
            #ew_child_dir = dir(new_directory.dir + "/" + child_dirs, depth, None)
            print(child_dirs)
            Recurse_directory_with_Depth(child_dirs + "/" + child_dirs)

    return new_directory.file_list

def print_with_depth(no_of_spaces,dir=True,same_dir=False):
        global depth
        x=" "
        if(same_dir):
            no_of_spaces=0
        if(not dir):
            print(x*no_of_spaces*2+"-f-",end=" ")
        else:
            print(x * no_of_spaces*1 + "-D-", end=" ")






if __name__== "__main__":
        file_count=0
        Dircount=0
        files_list=[]
        depth=0

        print("/Users/rob/PycharmProjects/Interview/Test")
        Recurse_directory_with_Depth("/Users/rob/PycharmProjects/Directory_tree")
        print("Total no of directories are",Dircount)
        print("Total no of files are",file_count)