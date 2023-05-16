file_type = {
    "pdf": "PDF(.pdf)",
    "docx": "Word文档(.docx)",
    "doc": "Word文档(.doc)",
    "xlsx": "Excel表格(.xlsx)",
    "xls": "Excel表格(.xls)",
    "csv": "逗号分隔(.csv)",
    "pptx": "演示文档(.pptx)",
    "ppt": "演示文档(.ppt)",
    "image": "图片文件(.png)",
    "txt": "纯文本(.txt)",
    "html": "网页文件(.html)",
    "json": "JSON(.json)",
}

source_file_type = {
    "pdf": "PDF(.pdf)",
    "docx": "Word文档(.docx)",
    "xlsx": "Excel表格(.xlsx)",
    "pptx": "演示文档(.pptx)",
    "image": "图片文件(.png)",
    # "txt": "纯文本(.txt)",
    # "html": "网页文件(.html)",
}


def get_can_convert_file_type(source):
    can_convert_file_type = {
        "pdf": ["docx", "image", "txt", "html"],
        "docx": ["pdf", "html", "txt"],
        # "doc": ["docx"],
        "xlsx": ["pdf", "json", "csv", "txt", "html"],
        # "xls": ["xlsx"],
        "pptx": ["pdf"],
        # "ppt": ["pptx"],
        "image": ["pdf"],
        "txt": ["pdf"],
        "html": ["pdf"],
    }
    return can_convert_file_type[source]
