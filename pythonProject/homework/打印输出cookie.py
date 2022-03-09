import os
import sqlite3
# 要pip pypiwin32
from win32crypt import CryptUnprotectData
)


# firefox
def get_firfox_cookie_path():
    cookiepath_common = os.environ['APPDATA'] + r"\Mozilla\Firefox\Profiles"
    print(cookiepath_common)
    folds_arr = os.listdir(cookiepath_common)
    folds_end = [os.path.splitext(file)[-1][1:] for file in folds_arr]
    print(cookiepath_common,folds_arr)
    for i in folds_end:
        print(i)
    if 'default-release' in folds_end:
        cookie_fold_index = folds_end.index('default-release')
    else:
        cookie_fold_index = folds_end.index('default')
    cookie_fold = folds_arr[cookie_fold_index]
    cookie_path = os.path.join(cookiepath_common, cookie_fold)
    return os.path.join(cookie_path, 'cookies.sqlite')