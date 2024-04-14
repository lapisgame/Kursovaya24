import json
from docx import Document
from docx.oxml.ns import qn

import os

# Функция для извлечения текста из ячейки
def get_cell_text(cell):
    texts = []
    for para in cell.findall(qn('w:p')):
        for run in para.findall(qn('w:r')):
            for text in run.findall(qn('w:t')):
                texts.append(text.text)
    return ' '.join(texts)

def docx_to_json(index, docx_path):
    res_json = {'index':0, 'title':'', 'content':''}
    # Загрузка документа DOCX
    doc = Document(docx_path)

    res_json['title'] = doc.paragraphs[0].text

    body_element = doc.element.body
    # Перебор всех элементов в теле документа
    for element in body_element:
        # Проверка, является ли элемент таблицей
        if element.tag == qn('w:tbl'):
            # Начало таблицы HTML
            html_table = '<table border="1">'
            
            # Перебор строк и ячеек таблицы
            for row in element.findall(qn('w:tr')):
                html_table += '<tr>'
                for cell in row.findall(qn('w:tc')):
                    cell_text = get_cell_text(cell)
                    html_table += f'<td>{cell_text}</td>'
                html_table += '</tr>'
            
            # Конец таблицы HTML
            html_table += '</table>'

            # Вывод HTML таблицы на экран
            res_json['content'] += html_table
        
        elif element.tag == qn('w:p'):
            # Перебор всех текстовых блоков (run) в параграфе
            text = ''
            for run in element.findall(qn('w:r')):
                this_text = run.text
                # Проверка, выделен ли текст жирным
                rPr = run.find(qn('w:rPr'))
                
                if rPr is not None:
                    b = rPr.find(qn('w:b'))
                    i = rPr.find(qn('w:i'))
                    if b is not None:
                        this_text = f"<b>{this_text}</b>"
                    if i is not None:
                        this_text = f"<i>{this_text}</i>"
                
                text += this_text
            res_json['content'] += f"{text}<br>"

        elif element.tag == qn('w:sectPr'):
            continue


    # Сохранение структуры содержимого в JSON
    res_json['title'] = res_json['title'].replace('<p>','').replace('</p>','')
    res_json['index'] = index

    with open(f'{docx_path[:-5]}.json', 'w', encoding='utf-8') as json_file:
        json.dump(res_json, json_file, ensure_ascii=False, indent=4)

    print("Содержимое документа сохранено в JSON.")
        


index = 0
docx_path = 'C:/Users/lapis/Desktop/Kursach24/qtLlearn/Lectures'
for filename in os.listdir(docx_path):
    if filename.endswith('.docx'):
        file_path = os.path.join(docx_path, filename)
        docx_to_json(index, file_path)
        index += 1