from helpers.mongo import cli

collection = cli["Zaid"]["rraid"]


async def gmute_user(chat):
    doc = {"_id": "Rraid", "users": [chat]}
    r = await collection.find_one({"_id": "Rraid"})
    if r:
        await collection.update_one({"_id": "Rraid"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


async def get_gmuted_users():
    results = await collection.find_one({"_id": "Rraid"})
    if results:
        return results["users"]
    else:
        return []


async def ungmute_user(chat):
    await collection.update_one({"_id": "Rraid"}, {"$pull": {"users": chat}})
