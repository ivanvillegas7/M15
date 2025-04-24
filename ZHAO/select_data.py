# -*- coding: utf-8 -*-

import os

def select_files(folder_path):
    """
    Selects files within a given folder based on the following criteria:
    1. Files should have a '.dat' extension.
    2. Selected files should have a size less than or equal to 5000 bytes.

    Args:
        folder_path (str): The path to the folder containing the files.

    Returns:
        list: A list of selected file paths that meet the specified criteria.
    """
    #Select all '.dat' files.
    data_files:  list[str]
    data_files = [f for f in os.listdir(folder_path) if f.endswith('.dat')]
    #Define where the files we are interested in are going to be stored.
    selected_files: list[str] = []
    #Get the file name.
    for file_name in os.listdir(folder_path):
        if file_name in data_files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                #Check its weight.
                if os.path.getsize(file_path) <= 5000:
                    #Save the file.
                    selected_files.append(file_path)
    #Return the files we are interested in.
    return selected_files

def join_files(folder_path, output_file, selected_files):
    """
    Combines the content of selected files into a single output file.

    Args:
        folder_path (str): The path to the folder containing the files.
        output_file (str): The name of the output file to be created.
        selected_files (list): A list of selected file paths to be combined.

    Returns:
        None
    """
    write_header: bool = True
    #Open the output file.
    with open(output_file, 'w') as output:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                #Check if we are interested in this particular file.
                if file_path in selected_files:
                    with open(file_path, 'r') as file:
                        if write_header:
                            #If the header is not written, do not do anything.
                            write_header = False
                        else:
                            #If it is, skip header from subsequent files.
                            for _ in range(4):
                                file.readline()
                        #Write the correspondent rows.
                        for line in file:
                            output.write(line)

def main():
    
    #Set the folder paths.
    paths = ['1', '2', '3', '4']
    #Set the global output file name.
    output_file_g = 'OutputMCMC_ZHAO.dat'
    for i in range(len(paths)):
        #Set the particular folder path.
        folder_path = f'MCMC_results/{paths[i]}'
        #Select the files we are interested in.
        selected_files = select_files(folder_path)
        #Join all the data from the files we are intersted in, in a single
        #output file.
        join_files(folder_path, output_file_g, selected_files)
    print(f"Data from all relevant files have been joined into {output_file_g}")

#Run the code.
main()
