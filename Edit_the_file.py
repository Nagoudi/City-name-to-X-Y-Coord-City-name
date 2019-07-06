#*********************************************************************************************

#                                         Main function                                      #

#*********************************************************************************************


#*********************************************** Starting ********************************************************************

def Processing_files (path_coordinates_File,path_corpus_File,Line_number_for_beginning_reading,Coordinate_Keywords,Coordinate_id_Keywords):
    # input
            #       path_coordinates_File                   ->  path file or files coordinates
            #       path_corpus_File                        ->  path file or files corpus
            #       Line_number_for_beginning_reading       ->  The beginning line of important information in the coordinates file
            #       Coordinate_Keywords                     ->  Locate the city name in the read line of the coordinates file
            #       Coordinate_id_Keywords                  ->  Locate the id name in the read line of the coordinates file



    Information_list =Prepare_the_information_from_the_coordinates_file (path_coordinates_File,Line_number_for_beginning_reading,Coordinate_Keywords,Coordinate_id_Keywords)

        #   Prepare the information we need from the coordinates file On the shape
            #   Information_list =
                #       [
                    #           [['Namecity1', ' coord0'],...]    // If the city name is single //
                    #           [['Namecity2', ' coord1 coord2 '],...]  // If the same city name and id are different //
                    #           [[' Namecity3 ', ' coord3'] ,[' Namecity4 ', ' coord4'],...]  // If the name of the city contained in the second //
                    #           [[' Namecity5 ', ' coord5'] ,[' Namecity6 ', ' coord6 coord7'],...] // All previous situations together //
                #       ]

    list_path_corpus_File = Extract_the_paths_of_each_file_inthe_folder (path_corpus_File,2)  #   It stores file paths corpus

    for Indicator_list_path_corpus_File in range (0,len(list_path_corpus_File)):   #   We go through all file paths in  list_path_corpus_File

        if(".txt" in list_path_corpus_File ):
            # file .txt
            f_corpus = open(list_path_corpus_File[Indicator_list_path_corpus_File] , "r", encoding="utf8")  #   We bring the file to read
            f_corpus1 = open(list_path_corpus_File[Indicator_list_path_corpus_File]+ "1", "w", encoding="utf8")  # We bring the file to write
                #  If the file size is large, it can not be uploaded to memory
                #   We create a file with the same path as the original file name but its extension is .txt1
                #   Click a line from the original file and then change it and retype it in the newly created file. Repeat the same process until we finish the entire file

            line_File_corpus = f_corpus.readline() # Line number one
            while (line_File_corpus != ""):
                #   Exit when reading the last line

                List_of_changes =[]  #We store the used diodes, which we have modified by the sentence

                for Indicator_Information_list in range (0,len(Information_list)):
                    #   We go on all the list
                    for Indicator_Internal_list_of_Information_list in range (0,len(Information_list[Indicator_Information_list])):
                        #   Within each list there is a list of lengths ranging from 1 to n
                                #           [['Namecity1', ' coord0'],...]  ,  // If the city name is single //
                                #           [['Namecity2', ' coord1 coord2 '],...]  , // If the same city name and id are different //
                                #           [[' Namecity3 ', ' coord3'] ,[' Namecity4 ', ' coord4'],...] ] , // If the name of the city contained in the second //
                                #           [[' Namecity5 ', ' coord5'] ,[' Namecity6 ', ' coord6 coord7'],...] // All previous situations together //
                        #   Reads from the last item in the list

                        if(Information_list[Indicator_Information_list][len(Information_list[Indicator_Information_list])-Indicator_Internal_list_of_Information_list-1][0] in line_File_corpus):

                            #   If the city is in the read line

                            List_of_changes.append([Information_list[Indicator_Information_list][len(Information_list[Indicator_Information_list])-Indicator_Internal_list_of_Information_list-1][0],Information_list[Indicator_Information_list][len(Information_list[Indicator_Information_list])-Indicator_Internal_list_of_Information_list-1][1]])
                                #   If the state in the read line store binary in the list of changes in order to decrease the search time on it is renewed
                            line_File_corpus = line_File_corpus.replace(Information_list[Indicator_Information_list][len(Information_list[Indicator_Information_list])-Indicator_Internal_list_of_Information_list-1][0],"["+Information_list[Indicator_Information_list][len(Information_list[Indicator_Information_list])-Indicator_Internal_list_of_Information_list-1][1]+"]")
                                #   Change city name to [id] . In order to avoid containing another city name

                for Indicator_List_of_changes in range (0,len(List_of_changes)):
                    #   We go on all the list
                    line_File_corpus = line_File_corpus.replace("["+List_of_changes[Indicator_List_of_changes][1]+"]",List_of_changes[Indicator_List_of_changes][0]+" "+List_of_changes[Indicator_List_of_changes][1])
                        #   Change [id]  name to city id
                f_corpus1.write(line_File_corpus)
                    #   Write the read line after the changes
                line_File_corpus=f_corpus.readline()
                    #   read line
            f_corpus.close()
                #   close
            f_corpus1.close()
                #   close

            import os
            os.remove(list_path_corpus_File[Indicator_list_path_corpus_File])
                #   Delete original  file
            os.rename(list_path_corpus_File[Indicator_list_path_corpus_File] + "1", list_path_corpus_File[Indicator_list_path_corpus_File])
                #   Rename the file created with the old file name

        if(".docx" in list_path_corpus_File):
            f_corpus = open(list_path_corpus_File[Indicator_list_path_corpus_File] , "r", encoding="utf8")  #   We bring the file to read

            # *******************************************************************************************************

            #                                         We will add it soon                                           #

            # *******************************************************************************************************

#*********************************************** end ********************************************************************



#*********************************************************************************************

#                      Prepare_the_information_from_the_coordinates_file                     #

#*********************************************************************************************

#*********************************************** Starting ********************************************************************

def Prepare_the_information_from_the_coordinates_file (path_coordinates_File,Line_number_for_beginning_reading,Coordinate_Keywords,Coordinate_id_Keywords):

    # input
            #       path_coordinates_File                   ->  path file or files coordinates
            #       Line_number_for_beginning_reading       ->  The beginning line of important information in the coordinates file
            #       Coordinate_Keywords                     ->  Locate the city name in the read line of the coordinates file
            #       Coordinate_id_Keywords                  ->  Locate the id name in the read line of the coordinates file


    Information_list_Final = []
        #   Fill Information coordinates list
    Information_list =[];
        #   Fill Information coordinates list
    list_path= Extract_the_paths_of_each_file_inthe_folder(path_coordinates_File,1)
        #   Preparing file paths for coordinates
    Indicator_list_path=0
    while(Indicator_list_path<len(list_path)):
        #   We go on all the list of path
        Information_list =Information_list+ Upload_file_coordinates(list_path[Indicator_list_path],Line_number_for_beginning_reading,Coordinate_Keywords,Coordinate_id_Keywords)
            #   Extract information from file coordinates
                #       [
                    #           ['Namecity1', ' coord1']    ,
                    #           ['Namecity2', ' coord2']    ,
                    #           ...,
                    #           ['Namecityn', ' coordn']
                #       ]
        Indicator_list_path=Indicator_list_path+1;
            #

    while(len(Information_list)>0):
            #   Starting from Information_list And access to
                #       [
                    #           [['Namecity1', ' coord0'],...]    // If the city name is single //
                    #           [['Namecity2', ' coord1 coord2 '],...]  // If the same city name and id are different //
                    #           [[' Namecity3 ', ' coord3'] ,[' Namecity4 ', ' coord4'],...]  // If the name of the city contained in the second //
                    #           [[' Namecity5 ', ' coord5'] ,[' Namecity6 ', ' coord6 coord7'],...] // All previous situations together //
                #       ]

        List_Similar_information_with_the_beginning_Information_list = [Information_list[0]]
            #   A temporary menu where the selected binaries are stored. Add the converging diodes
        Information_list=list(filter(lambda a: a != (Information_list[0]), (Information_list)))
            #  Delete the item from the list by repeating it

        Indicator_List_Similar_information_with_the_beginning_Information_list=0
        #   Indicator   of List_Similar_information_with_the_beginning_Information_list

        while(Indicator_List_Similar_information_with_the_beginning_Information_list<len(List_Similar_information_with_the_beginning_Information_list)):
            #   Pass all items in the temporary list one length and change their length if they are similar to one

            for Indicator in range(0,len(Information_list) ): # Search for cities with the same name and different in id
                #   Scroll all items in the initial menu
                if(len(Information_list)>Indicator):
                    #   We place a condition on the variable length by deletions in Information_list
                    if (Information_list[Indicator][0]==List_Similar_information_with_the_beginning_Information_list[Indicator_List_Similar_information_with_the_beginning_Information_list][0]):
                        #   If they had the same name
                        if(not ((Information_list[Indicator][1]) in (List_Similar_information_with_the_beginning_Information_list[Indicator_List_Similar_information_with_the_beginning_Information_list][1]))):
                            #   different id
                            List_Similar_information_with_the_beginning_Information_list.insert(Indicator_List_Similar_information_with_the_beginning_Information_list,[List_Similar_information_with_the_beginning_Information_list[Indicator_List_Similar_information_with_the_beginning_Information_list][0],List_Similar_information_with_the_beginning_Information_list[Indicator_List_Similar_information_with_the_beginning_Information_list][1]+" "+Information_list[Indicator][1]])
                                #   Add before the selected item
                            Information_list=list(filter(lambda a: a != (Information_list[Indicator]), (Information_list)))
                                #   delet in Information_list
                            List_Similar_information_with_the_beginning_Information_list.remove(List_Similar_information_with_the_beginning_Information_list[Indicator_List_Similar_information_with_the_beginning_Information_list+1])
                                #   delet the selected item
                else:
                    break

            for Indicator in range(0,len(Information_list) ): # Search for cities that intersect in the name
                if(len(Information_list)>Indicator):
                    #   We place a condition on the variable length by deletions in Information_list
                    if(List_Similar_information_with_the_beginning_Information_list[Indicator_List_Similar_information_with_the_beginning_Information_list][0] in Information_list[Indicator][0] ):
                        #
                        List_Similar_information_with_the_beginning_Information_list.append(Information_list[Indicator])
                            #   add
                        Information_list=list(filter(lambda a: a != (Information_list[Indicator]), (Information_list)))
                            #   delet in Information_list
                else:
                    break
            Indicator_List_Similar_information_with_the_beginning_Information_list=Indicator_List_Similar_information_with_the_beginning_Information_list+1
                #   Change the counter
            if (not (List_Similar_information_with_the_beginning_Information_list in Information_list_Final)):
                #   If the extracted small menu does not exist
                Information_list_Final.append(List_Similar_information_with_the_beginning_Information_list)
                    #   add in Information_list_Final
    return Information_list_Final

#*********************************************** end ********************************************************************



#*********************************************************************************************

#                         Extract the paths of each file inthe folder                         #

#*********************************************************************************************

#*********************************************** Starting ********************************************************************

def Extract_the_paths_of_each_file_inthe_folder (path_File,type_file):
         # input
            #       path_File                               ->  path file or files
            #       type_file                               -> if 1 is path file or Folder coordinates else path file or Folder corpus
    import glob
    import os
    list_path = []
         #  list_path
    if(type_file==1):
        #   path file or Folder coordinates
        if os.path.isdir(path_File):
            #   path Folder coordinates
            for Extracted_path in glob.glob(path_File+"\*"):
                #    Check everything in the folder
                if os.path.isfile (Extracted_path):
                    #   path file coordinates
                    if((".txt" in Extracted_path) or (".xlsx" in Extracted_path) or (".csv" in Extracted_path)):
                        #    path file  coordinates type txt or xlsx or csv
                        list_path.append(Extracted_path)
                            #    add path
                if os.path.isdir (Extracted_path):
                    #   path Folder coordinates
                    Extract_the_paths_of_each_file_inthe_folder(Extracted_path)
                        #    Call the regression function Extract_the_paths_of_each_file_inthe_folder
        else:
            #   path file  coordinates
            if((".txt" in path_File) or (".xlsx" in path_File) or (".csv" in path_File)):
                #      path file  coordinates type txt or xlsx or csv
                list_path.append(path_File)
                    #    add path
    else:
        #   path file or Folder corpus
        if os.path.isdir(path_File):
            #   path  Folder corpus
            for Extracted_path in glob.glob(path_File+"\*"):
                #    Check everything in the folder
                if os.path.isfile (Extracted_path):
                    #   path  file corpus
                    if((".txt" in Extracted_path) or (".docx" in Extracted_path) ):
                        #   path file  corpus type txt or docx
                        list_path.append(Extracted_path)
                            #   add path
                if os.path.isdir (Extracted_path):
                    #   path  Folder corpus
                    Extract_the_paths_of_each_file_inthe_folder(Extracted_path)
                    #   Call the regression function Extract_the_paths_of_each_file_inthe_folder
        else:
            #   path file  corpus
            if((".txt" in path_File) or (".docx" in path_File) ):
                #    path file  corpus type txt or docx
                list_path.append(path_File)
                     #  add path
    return list_path

#*********************************************** end ********************************************************************



#*********************************************************************************************

#                                Upload file coordinates information                         #

#*********************************************************************************************

#*********************************************** Starting ********************************************************************

def Upload_file_coordinates (path_coordinates_File,Line_number_for_beginning_reading,Coordinate_Keywords,Coordinate_id_Keywords):

    Information_list=[]
        # Information_list Fill Information coordinates list
    if(".txt" in path_coordinates_File):
        #   path file  coordinates type txt
        f_coordinates = open(path_coordinates_File, "r", encoding="utf8")
        #   We bring the file to read
        line_File_coordinates = f_coordinates.readline();
            #    Line number one
        while(Line_number_for_beginning_reading > 1):
            #   Find the desired line
            line_File_coordinates = f_coordinates.readline()
                #   Read the other line
            Line_number_for_beginning_reading=Line_number_for_beginning_reading+1
                #   Change the line cursor
        while (line_File_coordinates != ""):
            #   Exit when reading the last line
            Counter_9 = 0;
                # 9 is the numerical value of the letter \t.
            list =[]
                #   List of binaries [ city , id ]
            word = ""
                #    Variable word aggregation
            i = 0
                #
            while (i < len(line_File_coordinates)):
                #
                if (ord(line_File_coordinates[i]) != 9):
                    # \t
                    if(ord(line_File_coordinates[i])!=10):
                        # \n
                        word = word + line_File_coordinates[i]
                        #   Assembling the word
                else:
                    #
                    Counter_9 = Counter_9 + 1
                        #
                    if (Counter_9 == Coordinate_Keywords):
                        # End of the word
                        list.append(word)
                            #   add word Keywords -> city
                    if (Counter_9 == Coordinate_id_Keywords):
                        #
                        list.append(word)
                            #   add word id_Keywords -> id
                    word = ""
                        #    Variable word aggregation
                i = i + 1;
                    #

            if(Counter_9==4):
                #   End of the word
                list.append(word)
                    # add word id_Keywords -> id
            Information_list.append(list)
                #   add List of binaries [ city , id ] in line_File_coordinates
            line_File_coordinates = f_coordinates.readline();
                #   Read the other line
    if(".xlsx" in path_coordinates_File):
        #   path file  coordinates type xlsx
        import xlrd
        loc = (path_coordinates_File)
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)

            # For row 0 and column 0
        sheet.cell_value(0, 0)
        for x in range(Line_number_for_beginning_reading, sheet.nrows):
            # Read the other line
            Information_list.append([sheet.cell_value(x,Coordinate_Keywords-1),sheet.cell_value(x, Coordinate_id_Keywords-1)])
                # add [ city ,id ] in Information_list

    if(".csv" in path_coordinates_File):
        #   path file  coordinates type csv
        f_coordinates = open(path_coordinates_File, "r", encoding="utf8")

            # *******************************************************************************************************

            #                                         We will add it soon                                           #

            # *******************************************************************************************************

    return Information_list

#*********************************************** end ********************************************************************


path_coordinates_File="final_country_city_arabic.xlsx"
path_corpus_File="final_country_city_arabic.txt"
Line_number_for_beginning_reading=1
Coordinate_Keywords=2
Coordinate_id_Keywords=5

Processing_files(path_coordinates_File,path_corpus_File,Line_number_for_beginning_reading,Coordinate_Keywords,Coordinate_id_Keywords)
