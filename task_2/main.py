from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://yana:Trjam1987@catsdb.hbhulrz.mongodb.net/?retryWrites=true&w=majority&appName=CatsDB",
    server_api=ServerApi("1"),
)

db = client.book

# print(db)

# result_one = db.cats.insert_one(
#     {
#         "name": "barsik",
#         "age": 3,
#         "features": ["ходить в капці", "дає себе гладити", "рудий"],
#     }
# )

# print(result_one.inserted_id)

# result_many = db.cats.insert_many(
#     [
#         {
#             "name": "Lama",
#             "age": 2,
#             "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
#         },
#         {
#             "name": "Liza",
#             "age": 4,
#             "features": ["ходить в лоток", "дає себе гладити", "білий"],
#         },
#     ]
# )
# print(result_many.inserted_ids)

# # READ


def show_all_cats():
    """Show all cats"""
    result_all = db.cats.find({})
    for el in result_all:
        print(el)


# show_all_cats()


def show_cat(name):
    """Show a cat by name"""
    result = db.cats.findOne({"name": name})
    print(result)


# show_cat("Lama")

# Update


def update_cat_age(name, age):
    """Update cat's age by name"""
    db.cats.update_one({"name": name}, {"$set": {"age": age}})
    result = db.cats.find_one({"name": name})
    print(result)


# update_cat_age("Lisa", 5)


def add_feature(name, feature):
    """Add new feature to existing features by cat's name"""
    db.cats.updateOne({"name": name}, {"$addToSet": {"features": feature}})
    result = db.cats.find_one({"name": name})
    print(result)


# add_feature("Lisa", "Loves fish")

# Delete


def delete_cat(name):
    """Deletes cat from collection by cat's name"""
    db.cats.delete_one({"name": name})
    result = db.cats.find_one({"name": name})
    print(result)


# delete_cat("Lisa")


def delete_all_cats():
    """Deletes all cats from the cats collection"""
    result = db.cats.remove({})
    print(result)


# delete_all_cats()
