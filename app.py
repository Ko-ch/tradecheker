import os


def main():
    path_1 = os.path.join('C:\\Users', 'koich', 'OneDrive', 'デスクトップ', '04_app', '01_tradechecker', 'sampledata', )
    os.chdir(path_1)

    with open('EURUSD1.csv', mode='r', encoding='utf-8') as f:
        text = f.read()

if __name__ == "__main__":
    main()
