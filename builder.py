import os
print("Welcome to the Web Builder! \n Author: Prayag Yadav\n")
List = os.listdir()
#List.remove("default.html")
List = [ i for i in List if i not in ['LICENSE', 'README.md', '.git', 'default.html', 'builder.py', 'index.html'] ]
Location = os.getcwd()
print("List of directories: \n", List)
with open("default.html", "r") as template :
    lines = []
    for line in template :
        lines.append(line.strip())
    # print(lines[4])
    # print(lines[5])
    # print(lines[6])
    # print(lines[7])
    with open("index.html","w") as index :
        titleblock = f"<title> {Location} </title>\n"
        breadcrumb =f"<i> {Location} </i>\n</br>\n"
        Hyperlinks = []
        for f in List :
            Hyperlinks.append(f"<a href='{f}'>{f}</a>\n</br>\n")
        index.writelines(l+"\n" for l in lines[:5])
        index.writelines(titleblock)
        index.writelines(breadcrumb)
        index.writelines(l+"\n" for l in lines[5:7])
        index.writelines(Hyperlinks)
        index.writelines(l+"\n" for l in lines[7:])
print("Completed Building the index.html")
