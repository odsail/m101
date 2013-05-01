__author__ = 'scottrooke'

import pymongo
import sys
import traceback

#establish a connection to the database
connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string, safe=True)


#establish a connection to the students collections
db = connection.school
students = db.students


def drop_lowest_score():

    print("Dropping lowest score...")

    sort = [('_id',pymongo.ASCENDING)]



    try:
        data_filter = {'_id':True, 'scores':True}

        cursor = students.find({}, data_filter).sort(sort)
        for doc in cursor:
            lowScore = 101.0
            for scores in doc['scores']:
                scoreType = scores['type']
                if (scoreType == 'homework'):
                    score = scores['score']
                    if (score < lowScore):
                        lowScore = score

                print("Score type: ", scores['type'], " Score: ", scores['score'] )

            print("Lowest Score: ", lowScore)

            doc['scores'].remove({'type':'homework', 'score':lowScore})
            print (doc['scores'])

            students.update({'_id':doc['_id']},{'$set':{'scores':doc['scores']}})


    except:
#        print "Unexpected error:", sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print ("Error in %s on line %d" % (fname, lineno))
            print (sys.exc_info()[0],sys.exc_info()[1])



drop_lowest_score()