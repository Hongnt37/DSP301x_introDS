#import thư viện pandas và numpy
import pandas as pd
import numpy as np
#thiết lập không giới hạn độ rộng của cột, để hiển thị được toàn bộ dữ liệu của tất cả các cột
pd.set_option('display.max_colwidth', None)

#dữ liệu input từ người dùng
file_name = input("Enter a class to grade (i.e. class1 for class1.txt): ")
file_name = file_name + ".txt"
#kiểm tra file có tồn tại, in ra thông báo
try:
    with open(file_name, "r") as f:
        df = pd.read_csv(file_name, sep=" ", header=None)
        print("Successfully opened " + file_name)
except FileNotFoundError:
    print("File cannot be found.")

print("**** ANALYZING ****")
#đọc từng dòng dữ liệu của dataframe(df), check định dạng theo yêu cầu, in thông báo và xóa dòng không hợp lệ khỏi df
count_line = len(df)
indexes_to_drop = []
for i in range(len(df)):
    line = df.iloc[i]
    line = line.str.split(',', expand=True)
    if not line[0].str.match(r'N\d{8}').all():
        print("Invalid line of data: N# is invalid")
        print(df.iloc[i].to_string(index=False))
        indexes_to_drop.append(i)
    elif len(line.columns) != 26:
        print("Invalid line of data: does not contain exactly 26 values:")
        print(df.iloc[i].to_string(index=False))
        indexes_to_drop.append(i)
df = df.drop(indexes_to_drop)
df.reset_index(drop=True, inplace=True)

#nếu không có dòng lỗi thì in thông báo không có lỗi
if len(df) == count_line:
    print("No errors found!")
    
#in ra màn hình tổng số dòng hợp lệ; lỗi
print("**** REPORT ****")
print("Total valid lines of data: " + str(len(df)))
print("Total invalid lines of data: " +str(len(indexes_to_drop)))

#đáp án của đề thi
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer = answer_key.split(",")

#tạo file "class#_grades.txt" ghi kết quả thi của học sinh
file_expect_output = file_name.replace(".txt", "_grades.txt")
file = open(file_expect_output,"w")

#chấm điểm bài thi và lấy ra list câu hỏi bị bỏ qua và câu trả lời bị sai
student_score = []
skip_answer = []
incorrect_answer = []
for i in range(len(df)):
    score = 0
    line = df.iloc[i].to_string()
    line = line.split(",")
    # print(line)
    # print(len(line))
    for j in range(1,26):
        if line[j] == "":
            skip_answer.append(j)
        elif line[j] == answer[j - 1]:
            score += 4
        else:
            score += -1
            incorrect_answer.append(j)
    student_score.append(score)   
#ghi điểm vừa tính được vào file
    file.write(line[0] + "," + str(score) + "\n")

# Tính các chỉ số về điểm: lớn nhất, nhỏ nhất, trung bình, trung vị
highest_score = np.max(student_score)
lower_score = np.min(student_score)
mean = np.mean(student_score)
median = np.median(student_score)

#tạo hàm tính toán và trả về các giá trị mode- số lượng - tỷ lệ
def find_and_count_mode(lst, df):
    new_lst = [] 
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    lst_mode = []
    j1 = 0
    for i in new_lst:
        j2 = lst.count(i)
        if j2 > j1:
            lst_mode = [i]
            j1 = j2
        elif j2 == j1:
            lst_mode.append(i)
    lst_mode.sort()
    lst_return = []
    for i in lst_mode:
        j2 = lst.count(i)
        lst_return.append(str(i) +" - " + str(j2) +" - " + str("{:.2f}".format(j2/len(df))))
    return lst_return

# In ra các chỉ số đã tính toán được 
print("Total student of high scores: " + str(len(np.where(np.array(student_score) > 80)[0])))
print("Mean (average) score: {:.2f}".format(mean))
print("Highest score: " + str(highest_score))
print("Lowest score: " + str(lower_score))
print("Range of scores: " + str(highest_score - lower_score))
print("Median score: " + str(median))
print("Question that most people skip: " + ", ".join(find_and_count_mode(skip_answer, df)))
print("Question that most people answer incorrectly: " + ", ".join(find_and_count_mode(incorrect_answer, df)))
