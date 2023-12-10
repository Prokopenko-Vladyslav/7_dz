import shutil

def clean_folder(path):
    try:
        shutil.rmtree(path)
        print(f'Папка {path} успішно видалена')
    except FileNotFoundError:
        print(f'Папки {path} не існує')
    except PermissionError:
        print(f'Немає прав доступу для видалення {path}')
    except Exception as e:
        print(f'Виникла помилка при видаленні папки {path}: {e}')

def main():
    # Приклад використання:
    path = input('Введіть шлях до папки для видалення: ')
    clean_folder(path)

if __name__ == "__main__":
    main()