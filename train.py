#!/usr/bin/env python3

import model
import parse

def main():

    m = model.HaliteModel()
    #m.train_on_file(path)
    m.train_on_folder("./training")
    m.save(file_name="dt.svc")

    #print(clf.predict([[200,2,3,3,3,5,6]]))
    #data,result = m.train_on_file(path,winner) #files

main()

#  0: "o",
#  1: "w",
#  2: "n",
#  3: "e",
#  4: "s"}


# per ship
# north-cell : 2
# east-cell : 3
# south-cell : 4
# west-cell : 3
# turn : 123

# out
# origin = 0
# West = 1
# North = 2
# East = 3
# South = 4
