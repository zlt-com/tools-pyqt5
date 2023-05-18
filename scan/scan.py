from common import file_util


class ScanFile:
    def __init__(self, file="", keyword=[]):
        self.file = file
        self.keyword = keyword

    def parser_file(self):
        ext = file_util.get_file_ext(self.file)
        context = []
        key_has = []
        if ext == "docx":
            from docx import Document
            doc = Document(self.file)
            for paragraph in doc.paragraphs:
                for key in self.keyword:
                    if key in paragraph.text:
                        context.append(paragraph.text)
                        key_has.append(key)
            return ParserResult(self.file, key_has, context)
        else:
            return ParserResult()


class ParserResult:
    def __init__(self, file="", keys=[], context=[]):
        self.file = file
        self.keys = keys
        self.context = context

# cities = ['舆情', '秘密', '西藏']
# where = input("Where are you trying to find")
# if any(city in where for city in cities):
#     print("drive 5 miles")
