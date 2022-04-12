'''
Practicing implementing hashmaps
reference: codebasics on Youtube: https://www.youtube.com/watch?v=54iv1si4YCM
'''
# def get_hash(key):
#     h = 0
#     for char in key:
#         h += ord(char)
#     return h % 100

# out = get_hash('march 22')
# print(out)

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)] # initialized empty array [] instead of None

    # Hash function
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    # add/insert function
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        # self.arr[h] =val # overides index h, so it can't handle collisions yet
        found = False
        # istead create a linked list for when you need collision handling
        for idx, element in enumerate(self.arr[h]):
            # handling the case where the key exists already
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found=True
                break
        # handles the case where the key has not yet existed
        if not found:
            self.arr[h].append((key, val))
    
    # get function. Calling it by key
    def __getitem__(self, key):
        h = self.get_hash(key)
        # return self.arr[h] # retrieves everything in the particular index
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    
    #delete item function
    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

           

# t = HashTable()
# # using function
# # print(t.__setitem__('march 6', 130)) 
# # print(t.__getitem__('march 6'))

# print(t.get_hash('march 6'))
# print(t.get_hash('march 17'))

# # print('use dictionary: ')

# # using dictionary
# t['march 6'] = 120 # setitem
# t['march 6'] = 78 # updates 'march 6' value
# t['march 8'] = 67
# t['march 9'] = 4
# t['march 17'] = 459

# # print(t['march 6']) # getitem
# # print(t['march 8'])
# # print(t['march 9'])
# # print(t['march 17'])

# del t['march 6'] # should delete 130 from the dictionary

# print(t.arr) # printing dictionary
# # print(t['march 17'])

