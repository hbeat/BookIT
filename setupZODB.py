'''Setup
    pip install ZODB

   To use ZODB 
   The class that we will use it to store data need to inherit: 
            ClassName(persistent.Persistent):
                ...............

   Import
    import ZODB, ZODB.FileStorage, persistent, BTrees.OOBTree, transaction

   Connect DB
    storage = ZODB.FileStorage.FileStorage('nameDB.fs')
    db = ZODB>DB(storage)
    connection = db.open()
    root = connection.root
   
   To store data: do like dictionaries
    root.any_names = BTrees.OOBTree.Btree()
    e.g. root.classes = BTrees.OOBTree.Btree()
    root.classes['data-1'] = classData1
    root.classes['data-2'] = classData2
    ...

   To use data that we stored:
    return root.classes['data-1']

   Edit data:
    temp_variable = root.classes['data-1']
    temp_variable.method_define_in_the_class(arguments)
    transaction.commit()
'''


##pyuic5 -x file.ui -o filename.py