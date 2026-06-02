import argparse
import os


def create_folder(folder_name: str) -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, folder_name)
    os.mkdir(path)
    return path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Создать папку рядом со скриптом')
    parser.add_argument('-fn', '--folder-name', required=True, help='Имя папки')
    args = parser.parse_args()
    created = create_folder(args.folder_name)
    print(f'Папка создана: {created}')
