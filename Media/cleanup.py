import os
import shutil

# Settings
source_folder = '.'  # or use an absolute path
tmp_folder = "C:\\Users\\Danilo\\Desktop\\tmp"  # your external tmp location
filenames_to_keep = {
    '33-glavni-250507_1818.wav',
    '33-glavni-250507_1842.wav',
    '33-glavni-250507_1833-01.wav',
    '33-glavni-250507_1830-01.wav',
    '33-glavni-250507_1848-02.wav',
    '33-glavni-250507_1850-02.wav',
    '33-glavni-250507_1900-01.wav',
    '34-glavni-250507_1853-01.wav',
    '34-glavni-250507_1903-01.wav',
    '33-glavni-250507_1911-02.wav',
    '34-glavni-250507_1914-01.wav',
    '33-glavni-250507_1916-04.wav',
    '33-glavni-250507_1928.wav',
    '34-glavni-250507_1926-04.wav',
    '34-glavni-250507_1926-04.wav',
    '33-glavni-250507_1933-02.wav',
    '34-glavni-250507_1935-01.wav',
    '33-glavni-250507_1936-02.wav',
    '34-glavni-250507_1937.wav',
    '33-glavni-250507_2001-03.wav',
    '34-glavni-250507_2007.wav',
    '33-glavni-250507_2010-01.wav',
    '34-glavni-250507_2014.wav',
    '33-glavni-250507_2011-01.wav',
    '33-glavni-250507_2017.wav',
    '34-glavni-250507_2018.wav',
    '37-desno-250507_1953-02.wav',
    '38-levo-250507_1959.wav',
    '38-levo-250507_1957-01.wav',
    '33-glavni-250507_2022.wav',
    '34-glavni-250507_2022-01.wav',
    '34-glavni-250507_2024-01.wav',
    '33-glavni-250507_2024.wav',
    '33-glavni-250507_2027-03.wav',
    '34-glavni-250507_2028-01.wav',
    '33-glavni-250507_2030.wav',
    '33-glavni-250507_2034-02.wav',
    '34-glavni-250507_2032-01.wav',
    '35-podebljavanje-250507_2050.wav',
    '35-donja oktava-250507_2043.wav'
    '36-growl-250507_2044.wav',
    '33-glavni-250507_2034-02.wav',
    '34-glavni-250507_2036.wav',
    '33-glavni-250507_2038.wav'


}
run_mode = True  # Set to True to actually move the files

# Ensure tmp folder exists
if run_mode and not os.path.exists(tmp_folder):
    os.makedirs(tmp_folder)

# Process
for filename in os.listdir(source_folder):
    src_path = os.path.join(source_folder, filename)
    dst_path = os.path.join(tmp_folder, filename)

    if filename in filenames_to_keep or filename[0] != '3' or not os.path.isfile(src_path):
        continue

    if run_mode:
        shutil.move(src_path, dst_path)
        print(f"Moved: {filename} -> {tmp_folder}")
    else:
        print(f"[Dry Run] Would move: {filename}")

print("Done.")
