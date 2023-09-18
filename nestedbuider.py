def makeindex(directory_name):
    os.chdir(directory_name)
    List = os.listdir()
    List = [ i for i in List if i not in ['LICENSE', 'README.md', '.git', 'default.html', 'builder.py', 'index.html'] ]
    ListDir = [i for i in List if os.path.isdir(i)]
    Location = os.getcwd()
    print("List of directories: \n", ListDir)
    print("Full List: \n", List)
    with open("default.html", "r") as template :
        lines = []
        for line in template :
            lines.append(line.strip())
        with open("index.html","w") as index :
            titleblock = f"<title> {Location} </title>\n"
            breadcrumb =f"<i> {Location} </i>\n</br>\n"
            heading = (Location.split("/"))[-1]
            headingblock = f"<h1>{heading}</h1>\n</br>\n"
            Hyperlinks = []
            for f in List :
                Hyperlinks.append(f"<a href='{f}'>{f}</a>\n</br>\n")
            index.writelines(l+"\n" for l in lines[:5])
            index.writelines(titleblock)
            index.writelines(breadcrumb)
            index.writelines(headingblock)
            index.writelines(l+"\n" for l in lines[5:7])
            index.writelines(Hyperlinks)
            index.writelines(l+"\n" for l in lines[7:])
            if len(ListDir) == 0 :
                return
            for i in ListDir :
                makeindex(i)
            os.chdir("../")
    return 

import os
print("Welcome to the Web Builder! \n Author: Prayag Yadav\n")
rootdirname = ((os.getcwd()).split("/"))[-1]
os.chdir("../")
makeindex(os)
print("Completed Building the index.html")

