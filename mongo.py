import pymongo
import datetime
from flask import Flask,request

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://AhmadYR:bismillah@restect-shard-00-00.oe61b.mongodb.net:27017,restect-shard-00-01.oe61b.mongodb.net:27017,restect-shard-00-02.oe61b.mongodb.net:27017/?ssl=true&replicaSet=atlas-1332jq-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client['ayura']
my_collections = db['bebas']

@app.route('/location',methods = ['GET','POST'])
def location():
    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    if request.method == 'POST' :
        result = my_collections.insert_one({"kecepatan":kecepatan,"latitude":latitude,"longitude":longitude})
        print(result)
        return {
            "output":{
                "kecepatan": kecepatan,
                "latitude": latitude,
                "longitude": longitude,
                "timestamp": datetime.datetime.now()
                    }
            }

if __name__ == '__main__':
    app.run(debug=True)