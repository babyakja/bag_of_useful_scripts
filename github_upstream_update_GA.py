import os
import git

currentDir = os.getcwd() # Get Current directory

all_directories = os.listdir(currentDir) # list all folders
for dir in all_directories:
    if dir == 'upstream_fill.py':
        pass
    elif dir == '.DS_Store':
        pass
    else:
        git_dir = os.path.join(currentDir, dir)
        print(git_dir)
        os.chdir(git_dir)
        # Step 1 - make sure you have pulled and are up to date
        g = git.cmd.Git(git_dir)
        g.pull()
        # Step 2 - add upstream to DSI
        os.system("git remote add upstream " + "https://git.generalassemb.ly/DSI-US-5/" + dir + ".git")
        # Step 2a if upstream already set
        #os.system("git remote set-url upstream " + "https://git.generalassemb.ly/DSI-US-5/" + dir + ".git")
        # Step 3 - pull upstream master after setting
        os.system("git pull upstream master")
