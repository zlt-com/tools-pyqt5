class ConverterFactory:
    def __init__(self, ext: str):
        super(ConverterFactory, self).__init__()
        self.ext = ext

    def get_converter(self):
        if self.ext == "pdf":
            from fileconv.pdf import PDFConverter
            return PDFConverter()
        elif self.ext == "xlsx":
            from fileconv.excel import ExcelConverter
            return ExcelConverter()
        elif self.ext == "csv":
            from fileconv.csv import CsvConverter
            return CsvConverter()
        elif self.ext == "json":
            from fileconv.json import JsonConverter
            return JsonConverter()
        elif self.ext == "txt":
            from fileconv.text import TxtConverter
            return TxtConverter()
        elif self.ext == "docx":
            from fileconv.word import DocxConverter
            return DocxConverter()
        elif self.ext == "html":
            from fileconv.html import HtmlConverter
            return HtmlConverter()
        elif self.ext == "image":
            from fileconv.image import ImageConverter
            return ImageConverter()
