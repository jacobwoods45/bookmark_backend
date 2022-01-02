from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://jacobwoods45:lark1241@upmarky-cluster.lhynt.mongodb.net/Upmarky?retryWrites=true&w=majority')
db = cluster["Upmarky"]
links = db["Links"]



def insert_link(link, date, device):
    post = {"link": link,
        "date": date,
        "device": device
        }
    links.insert_one(post).inserted_id
def get_all_links():
    links_array = []
    document_object = links.find({})
    for document in document_object:
          links_array.append(document["link"])
    print(links_array)
    return links_array

