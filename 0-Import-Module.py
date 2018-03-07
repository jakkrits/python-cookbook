import module_test
import sys

print(module_test.workers)

# path that python looks for files
print(sys.path)

# if module not in SYS.PATH you have to append it to the SYS.PATH
# sys.paht('..PATH..')
# OR
# spec that path in .bash_profile
# export PYTHONPATH="..PATH_OF_THE_MODULE.."
