from Data_Preprocessing import Preprocessing
import os, glob


def get_latest_file():
    current_dir =  os.path.abspath(os.path.dirname(__file__))
    dir_path = os.path.abspath(current_dir + "/../../Data")
    list_of_files = glob.glob(dir_path + '/*.tsv')
    return max(list_of_files, key=os.path.getctime)


def main():
    
    dp = Preprocessing(get_latest_file())
    
    dp.remove_special_characters_multi()
    
    dp.file()
    
    

    
    
    
    '''do file operations here'''


if __name__ == '__main__':
    main()