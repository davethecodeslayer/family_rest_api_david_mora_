from random import randint

class FamilyStructure:
    
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": self.last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        },
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": self.last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        },
        {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age": 5,
            "lucky_numbers": [1]
        }]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):

        if member["id"] == None:
            new_id = self._generateId()
        else:
            new_id = member["id"]

        persona = [{
            "id": new_id,
            "first_name": member["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        }]
        self._members.append(persona)
        return persona

    def delete_member(self, id):
        self._members = list(filter(
            lambda member : member["id"] != id, self._members
        ))
        return True

    def get_member(self, id):
        for member in self._members : 
            if member["id"] == id:
                return member
        
        return None

    def get_all_members(self):
        return self._members
