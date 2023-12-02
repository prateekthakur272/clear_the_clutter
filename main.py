import os

def get_files(dir_path,ext):
    try:
        os.chdir(dir_path)
    except FileNotFoundError as e:
        print(f'path \'{dir_path}\' does not exist')
    except Exception as e:
        print(e)
    
    cur_dir = os.getcwd()
    items = os.listdir(cur_dir)
    items = list(filter(lambda item:item.lower().__contains__(f'.{ext.lower()}'),items))
    return sorted(items)

def rename(items, ext):
    count = 0
    for item in items:
        if not f'{count}.{ext}' in items:
            print(f'renaming {item} to {count}.{ext}')
            os.rename(item,f'{count}.{ext}')
        count+=1
    print('Done')
    
    
if __name__ == '__main__':
    
    dir_path = input("Enter path to directory: ")
    file_ext = input('Enter file extension: ')

    items = get_files(dir_path,file_ext)
    for item in items:
        print(item)
    
    if items:
        print(f'found {len(items)} files of type {file_ext}\nproceed to rename?(y/n)')  
        choice = input()
        match choice:
            case 'y':
                rename(items,file_ext)
            case _:
                print('Exit')
    else:
        print('found nothing')