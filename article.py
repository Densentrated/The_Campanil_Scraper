class article:
    def __init__(self, title, author, data, genre, content):
        self.title = title
        self.content = content
        self.author = author
        self.genre = genre
        self.date = data

    def display(self):
        print(f"title: {self.title}\nauthor: {self.author}\ngenre: {self.genre}\ndate: {self.date}\n")
        #print(self.content)