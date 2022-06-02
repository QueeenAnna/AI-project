import os


def main():
    label_img_path = os.path.join('code', 'repo')
    if not os.path.exists(label_img_path):
        if os.name == 'posix':  # Mac, Linux
            os.system(f'mkdir -p {label_img_path}')
        if os.name == 'nt':  # Windows
            os.system(f'mkdir {label_img_path}')

        os.system(f'git clone https://github.com/tzutalin/labelImg {label_img_path}')

        if os.name == 'posix':
            os.system(f'cd {label_img_path} && make qt5py3')
        if os.name == 'nt':
            os.system(f'{label_img_path} && pyrcc5 -o libs/resources.py resources.qrc')

    os.system(f'cd {label_img_path} && python labelImg.py')


if __name__ == '__main__':
    main()
