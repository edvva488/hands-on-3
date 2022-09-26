import md

md.run_md()

from os.path import exists

file_exists = exists("cu.traj")
print(file_exists)
