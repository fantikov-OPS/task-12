import argparse
import os


def create_folder_and_file(folder_name: str, file_name: str) -> tuple[str, str]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, folder_name)
    os.mkdir(folder_path)
    file_path = os.path.join(folder_path, file_name)
    open(file_path, 'a', encoding='utf-8').close()
    return folder_path, file_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Создать папку и файл в ней (рядом со скриптом)',)
    parser.add_argument('-fn', '--folder-name', required=True, help='Имя папки')
    parser.add_argument('-file', '--file-name', required=True, help='Имя файла')
    args = parser.parse_args()
    folder_path, file_path = create_folder_and_file(args.folder_name, args.file_name)
    print(f'Папка создана: {folder_path}')
    print(f'Файл создан: {file_path}')
