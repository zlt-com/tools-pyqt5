from docx2pdf import convert
import docx2txt
import os
import mammoth
from common import file_util


def docx_to_pdf(source_file):
    out_file_name = file_util.get_output_path(source_file, '.pdf')
    if os.path.exists(out_file_name):
        os.remove(out_file_name)
    convert(source_file, out_file_name)
    return out_file_name


def docx_to_txt(source_file):
    out_file_name = file_util.get_output_path(source_file, '.txt')
    text = docx2txt.process(source_file)
    out_file = open(out_file_name, "w", encoding='utf-8')
    out_file.write(text)
    out_file.close()
    return out_file_name


def docx_to_html(source_file):
    out_file_name = file_util.get_output_path(source_file, '.html')
    with open(source_file, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value
        out_file = open(out_file_name, "w", encoding='utf-8')
        out_file.write(html)
        out_file.close()
    return out_file_name
