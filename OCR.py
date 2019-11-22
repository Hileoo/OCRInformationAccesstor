import cv2
from aip import AipOcr


def print_operation(lists, index):
    file_data=open('data.txt','a')
    print("\nUser number: %d"%index)
    file_data.write("\nUser number: %d"%index)
    lists=lists[4:]
    for result in lists:
        text = result["words"]
        if(text=="签到足迹" or text=="赞" or text=="他推荐的分组" or text=="她推荐的分组"):
            break
        elif(text=="账号信息"):
            print(text+":")
            file_data.write("\n"+text+":\n")
        elif(text=="个人信息"):
            print("\n"+text+":")
            file_data.write("\n"+text+":")
        else:
            print(text, end=' ')
            file_data.write(text+" ")
    file_data.close()


def write_frame(lists,fname):
    img = cv2.imread(fname)
    for result in lists:
        text = result["words"]
        location = result["location"]
        cv2.rectangle(img, (location["left"],location["top"]), (location["left"]+location["width"],location["top"]+location["height"]), (0,255,0), 2)
    cv2.imwrite("results_pic/"+fname[7:-4]+"_result.jpg", img)


def read_operation(file_path):
    APP_ID = '16208010'
    API_KEY = 'sGIcNgEzfFaLz7Hx4NM2bBuR'
    SECRET_KEY = 'OH7IWY8ymr5FArY8h8UoMZRqkrZy1UxY'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()


    image = get_file_content(file_path)
    results = client.general(image)["words_result"]
    return results


def ocr_function(file_path, index):
    results=read_operation(file_path)
    write_frame(results, file_path)
    print_operation(results, index)

