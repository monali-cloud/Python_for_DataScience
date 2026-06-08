class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        
    def show(self):
        print("Title :",self.title)
        print("Author :",self.author)

class Novel(Book):
    pass

b1=Novel("verity","Collen Hoover")

b1.show()