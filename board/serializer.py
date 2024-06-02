import json


class BoardSerializer:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def from_body(cls, request):
        return json.loads(request.body)

    @classmethod
    def from_request(cls, request):
        title = request.POST.get("title")
        content = request.POST.get("content")
        return cls(title=title, content=content)

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
        }