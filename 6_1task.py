from errno import EEXIST
from importlib.metadata import files
from ntpath import join
import os
from posixpath import dirname
import shutil
#from pathlib import Path

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЩЪЫЬЭЮЯЄІЇҐ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g", "A", "B", "V", "G", "D", "E", "E", "J", "Z", "I", "J", "K", "L", "M", "N", "O", "P", "R", "C", "T", "U",
               "F", "H", "TS", "CH", "SH", "SCH", "", "Y", "", "E", "YU", "U", "JA", "JE", "JI", "G")

Trans = {}

def normalize(localename):
    result = ''
    for c,l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        Trans[ord(c)] = l    
    result_term = localename.translate(Trans)
    for li in result_term:
        if (48 <= ord(li) <= 57) or (65 <= ord(li) <= 90) \
            or (97 <= ord(li) <= 122) or (ord(li) == 32):
            result = result + li    
            continue
        else:
            li = '_'
            result = result + li
    result = result.strip()            
    print(result)
    return result

def sort_n_clear (list_name):
    #  удаляет лишние элементы из списков файлов и расширений 
    new_list = []
    [new_list.append(item) for item in list_name if item not in new_list]
    return new_list

def folder_sorter(folder_path):
    text_list = []
    imgs_list = []
    vid_list = []
    audio_list = []
    arch_list = []
    unscr_list = []
    full_list = []
    file_ext_unname = []
    file_name_betw = ''

    for file_name in os.listdir(folder_path):
        if os.path.exists(os.path.join(folder_path, file_name)):
            if os.path.isfile(os.path.join(folder_path, file_name)):
                name, file_ext = os.path.splitext(file_name)
                if (file_ext == '.txt') or (file_ext == '.doc') \
                    or (file_ext == '.docx') or (file_ext == '.pdf') \
                    or (file_ext == '.xls') or (file_ext == '.pptx'):
                    
                    file_name_betw = normalize(name) + file_ext
                    os.replace(os.path.join(folder_path, file_name),os.path.join(folder_path, file_name_betw))            
                    print(file_name_betw)
                    try:
                        os.mkdir(os.path.join(folder_path, 'Text'))
                        shutil.move(os.path.join(folder_path, file_name_betw), os.path.join(folder_path, 'Text'))
                    except FileExistsError:
                        shutil.move(os.path.join(folder_path, file_name_betw), os.path.join(folder_path,'Text'))
                    except EEXIST:
                        continue
                    text_list.append(file_name)
                    full_list.append(file_ext)
                    
                elif (file_ext == '.jpeg') or (file_ext == '.png') \
                    or (file_ext == '.jpg') or (file_ext == '.svg'):
                    
                    file_name_betw = normalize(name) + file_ext
                    os.replace(os.path.join(folder_path, file_name),os.path.join(folder_path, file_name_betw))            
                    print(file_name_betw)
                    try:
                        os.mkdir(os.path.join(folder_path, 'Images'))
                        shutil.move(os.path.join(folder_path, file_name_betw), os.path.join(folder_path, 'Images'))
                    except FileExistsError:
                        shutil.move(os.path.join(folder_path, file_name_betw), os.path.join(folder_path,'Images'))
                    except EEXIST:
                        continue
                    imgs_list.append(file_name)
                    full_list.append(file_ext)
                    print(file_ext)
                    
                elif (file_ext == '.avi') or (file_ext == '.mp4') \
                    or (file_ext == '.mov') or (file_ext == '.mkv'):
                    
                    file_name_betw = normalize(name) + file_ext
                    os.replace(os.path.join(folder_path, file_name),os.path.join(folder_path, file_name_betw))            
                    print(file_name_betw)
                    try:
                        os.mkdir(os.path.join(folder_path, 'Video'))
                        shutil.move(os.path.join(folder_path, file_name_betw), os.path.join(folder_path, 'Video'))
                    except FileExistsError:
                        shutil.move(os.path.join(folder_path, file_name_betw), os.path.join(folder_path,'Video'))
                    except EEXIST:
                        continue
                    vid_list.append(file_name)
                    full_list.append(file_ext)
                
                elif (file_ext == '.mp3') or (file_ext == '.ogg') \
                    or (file_ext == '.wav') or (file_ext == '.amr'):
                    
                    name_of_dir = 'Audio'
                    file_name_betw = normalize(name) + file_ext
                    os.replace(os.path.join(folder_path, file_name),os.path.join(folder_path, file_name_betw))            
                    print(file_name_betw)
                    try:
                        os.mkdir(os.path.join(folder_path, 'Audio'))
                        shutil.move(os.path.join(folder_path, file_name_betw), os.path.join(folder_path,'Audio'))
                    except FileExistsError:
                        shutil.move(os.path.join(folder_path, file_name_betw), os.path.join(folder_path,'Audio'))
                    except EEXIST:
                        continue
                    audio_list.append(file_name)
                    full_list.append(file_ext)
                
                elif (file_ext == '.zip') or (file_ext == '.gz') \
                    or (file_ext == '.tar'):
                    

                    file_name_betw = normalize(name) + file_ext
                    os.replace(os.path.join(folder_path, file_name),os.path.join(folder_path, file_name_betw))            
                    print(file_name_betw)
                    try:
                        arch_pas = os.path.join(folder_path,'Archive')
                        os.mkdir(arch_pas)
                        shutil.move(os.path.join(folder_path, file_name_betw), arch_pas)
                    except FileExistsError:
                        shutil.move(os.path.join(folder_path, file_name_betw), arch_pas)
                    except EEXIST:
                        continue
                    shutil.unpack_archive(os.path.join(arch_pas, file_name_betw),arch_pas)
                    arch_list.append(file_name)
                    full_list.append(file_ext)
                
                else:                
                    file_name_betw = normalize(name) + file_ext
                    os.replace(os.path.join(folder_path, file_name),os.path.join(folder_path, file_name_betw))
                    print(file_name_betw)
                    try:
                        os.mkdir(os.path.join(folder_path, 'Unscrible'))
                        shutil.move(os.path.join(folder_path, file_name_betw), os.path.join(folder_path, 'Unscrible'))
                    except FileExistsError:
                        shutil.move(os.path.join(folder_path, file_name_betw), os.path.join(folder_path,'Unscrible'))
                    except EEXIST:
                        continue
                    unscr_list.append(file_name)
                    file_ext_unname.append(file_ext)
            elif os.path.isdir(os.path.join(folder_path, file_name)): 
                print ('C>LF')
                try:
                    os.rmdir(os.path.join(folder_path, file_name))
                except OSError:
                    if (file_name == 'Text') or (file_name == 'Video') or (file_name == 'Audio') or (file_name == 'Images') or (file_name == 'Archive') or (file_name == 'Unscrible'):
                        continue
                    else:    
                        folder_sorter(os.path.join(folder_path, file_name))           
                        print('YEEEEE')
        
    sort_n_clear (file_ext_unname)
    sort_n_clear (text_list)
    sort_n_clear (imgs_list)
    sort_n_clear (vid_list)
    sort_n_clear (audio_list)
    sort_n_clear (arch_list)
    sort_n_clear (unscr_list)
    sort_n_clear (full_list)
    
    return full_list
    

answer = input('Give me a pass:  ')
folder_sorter(answer)
    
