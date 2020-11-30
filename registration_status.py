import json
def read_reg_info_from_file():

    try:
        # Open the file as readonly mode
        file = open("Registration_info.json", "r")

        # Read data from file
        file_content_as_text = file.read()

        # convert json text to array
        info_array = json.loads(file_content_as_text)

        # close the file
        file.close()

        return info_array
    except:
        return []

def write_reg_info_to_file(info):

    # Open the file with write permission
    file = open("Registration_info.json", "w+")

    # Convert python list to json text
    json_data = json.dumps(info, indent=4)

    # save the text to the contacts.json file
    file.writelines(json_data)

    # close the file
    file.close()


def add_reg_info(std_id,std_name,reg_stat,lc):
    # Read all reg info from file
    info_array = read_reg_info_from_file()

    new_info=dict()
    new_info["ID"]= std_id
    new_info["Name"]= std_name
    new_info["Registration Staus"]= reg_stat
    new_info["Course List"]=lc

    # Add the new reg info  into the info array
    info_array.append(new_info)

    # Write the new array into the file
    write_reg_info_to_file(info_array)

def search_info(id):

    # Read all reg  info from file
    info_array=read_reg_info_from_file()

    for info in info_array:
        if info.get("ID")==id:
            return info

    write_reg_info_to_file(info_array)

    return None

def update_reg_stat(id,status):
    # Read all reg info from file
    info_array = read_reg_info_from_file()

    for info in info_array:
        b=0
        if info.get("ID")==id:
            info["Registration Staus"]= status
            b=1
            break

        else:
            b=0
     # Write the Updated value into the file
    write_reg_info_to_file(info_array)
    return b

def delete_record(id):
    # Read all reg info from file
    info_array = read_reg_info_from_file()

    # Delete the desired record
    for info in info_array:
        b=0
        if info.get("ID")==id:
            info.pop("ID")
            info.pop("Name")
            info.pop("Registration Staus")
            info.pop("Course List")
            b=1
            break
        else:
            b=0

    write_reg_info_to_file(info_array)
    return b


# Execution part
while True:
    print("------------1. Add New Student's Info-------------")
    print("------------2. Search Student's Info--------------")
    print("------------3. Update Registration Status---------")
    print("------------4. Delete Student's Record------------\n")

    print("What's your Choice???😇😇😇😇")
    select=int(input())

    if select==1:
        print("Enter ID: " ,end="")
        std_id=str(input())
        print("Enter Name: ", end="")
        std_name= str(input())
        print("Enter Registration Status: ", end="")
        reg_stat=str(input())
        lc=[]
        print("Enter The Number of Courses Taken: ",end="")
        n=int(input())
        print("Enter Course name, Course code & Section Name in one line by 'Coma':")
        for c in range(0,n):
            ele= str(input())
            lc.append(ele)

        add_reg_info(std_id, std_name, reg_stat,lc)
        print("Information Recorded👍👍\n")

    elif select==2:
        print("Enter the ID you want to search : ", end="")
        id=str(input())
        search_result=search_info(id)
        print("Search Result of ID '{}' is:\n\n----Student's Name : {}\n"
              "----Student's ID   : {}\n----Registation    : {}\n----Course Taken   : {}\n\n".format(
            id, search_result["Name"], search_result["ID"],
            search_result["Registration Staus"],search_result["Course List"])if search_result is not None else"Record Doesn't Exist\n")

    elif select==3:
        print("Enter the ID you want to update: ", end="")
        id=str(input())
        print("Enter updated Status: ", end="")
        sts=str(input())

        updated_result=update_reg_stat(id,sts)
        print("Registration Status Updated👍👍👍\n"if updated_result ==1 else "Doesn't Exist\n")

    elif select==4:
        print("Enter the ID you want to delete : ", end="")
        id = str(input())

        del_result=delete_record(id)
        print("Record deleted successfully.\n"if del_result==1 else "Doesn't Exist\n")











