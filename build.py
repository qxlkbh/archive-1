import glob
import shutil
import os
import os.path
import distutils.dir_util

shutil.rmtree("build", ignore_errors=True)
os.mkdir("build")

distutils.dir_util.copy_tree("bees", "build")
distutils.dir_util.copy_tree("comics", "build/comics")

l = [i[6:]
     for i in glob.glob('build/**/*', recursive=True) if os.path.isfile(i)]

print(*l, sep='\n', file=open("build/index.html", "w"))
