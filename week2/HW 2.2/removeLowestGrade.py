__author__ = 'scottrooke'

import pymongo, sys
connection = pymongo.Connection("mongodb://localhost",safe=True)
db=connection.students
### s1 for sample (a cursor (iterable)); sort first by "student_id"
s1=db.grades.find({"type":"homework"}).sort([("student_id", pymongo.ASCENDING),("score", pymongo.DESCENDING)])
### c1 is a counter; note every 2nd record will be the lower score for that student
c1=1
for d in s1: # d for document
    id1=d["_id"] # id1 is particular id
    if c1%2==0: # c1 divisible by 2?
        db.grades.remove({"_id":id1})
    c1=c1+1
