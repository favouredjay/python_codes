class unique:
    is_unique = False


 def unique_string(self, word):
    for i in self.word:
        for j in range(1, word - 1):
            if j in i:
                return False
            else:
                return True


x = unique
x.unique_string("struggle")
