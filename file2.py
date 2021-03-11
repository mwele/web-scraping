import file1
print("File two __name__ is set to:{}".format(__name__))
'''The variable __name__ for the file/module that is run will be always __main__.
 But the __name__ variable for all other modules that are being imported will be set to their module's name.'''