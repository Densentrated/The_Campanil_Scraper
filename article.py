import json

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

    def to_dict(self):
        return {"title": self.title, "author": self.author, "genre": self.genre, "date": self.date, "content": self.content}
    
    def to_json(self):
        return json.dumps(self.to_dict())
    
    def to_csv(self):
        return f'"{self.title}","{self.author}","{self.genre}","{self.date}","{self.content}"'