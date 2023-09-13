# DSP301x_ASM2
# Hướng dẫn về Dự án

## Mô tả
Dự án này là một chương trình đơn giản sử dụng Python để phân tích, chấm điểm và đánh giá bài làm của học sinh dựa trên kết quả đầu vào từ các file "class#.txt" với # là mã lớp

## Yêu cầu
Trước khi bạn bắt đầu, hãy đảm bảo rằng bạn đã cài đặt các thư viện sau của Python:
- pandas
- numpy
Bạn có thể cài đặt chúng bằng cách sử dụng pip: !pip install pandas numpy

## Sử dụng
1. Chạy chương trình bằng cách chạy file Python "lastname_firstname_grade_the_exams.py".
2. Chương trình sẽ yêu cầu bạn nhập tên của lớp bạn muốn đánh giá (ví dụ: "class1").
   Nếu bạn nhập sai tên lớp hoặc dữ liệu đầu vào không có thông tin về lớp học bạn đang muốn xem chương trình sẽ trả về thông báo: "File cannot be found."
   Ngược lại chương trình sẽ thông báo: "Successfully opened class#.txt" 
4. Chương trình sẽ đọc dữ liệu từ tệp văn bản tương ứng và thực hiện phân tích.

## Kết quả
Sau khi chạy, ứng dụng sẽ cung cấp thông tin sau:
- In ra những dòng dữ liệu sai không hợp lệ và chi tiết lỗi: "Invalid line of data: N# is invalid" hoặc "Invalid line of data: does not contain exactly 26 values:" hoặc cả hai.
- báo cáo tổng số dòng dữ liệu hợp lệ và không hợp lệ có trong file.
- Chấm điểm tất cả học sinh có dữ liệu đầu vào hợp lệ theo đáp án và barem điểm có sẵn.
- Cung cấp các chỉ số: số lượng học sinh đạt điểm cao (>80), điểm trung bình, điểm cao nhất, điểm thấp nhất, miền giá trị của điểm (điểm cao nhất - điểm thấp nhất), điểm trung vị 
- Cung cấp các câu hỏi bị học sinh bỏ qua nhiều nhất theo thứ tự: số thứ tự câu hỏi - số lượng học sinh bỏ qua -  tỉ lệ bị bỏ qua (nếu có cùng số lượng cho nhiều câu hỏi bị bỏ thì liệt kê theo thứ tự của câu hỏi).
- Cung cấp các câu hỏi bị học sinh làm sai nhiều nhất theo thứ tự: số thứ tự câu hỏi - số lượng học sinh bỏ qua -  tỉ lệ bị bỏ qua (nếu có cùng số lượng cho nhiều câu hỏi bị bỏ thì liệt kê theo thứ tự của câu hỏi)
- Cung cấp file "class#_grades.txt" chứa mã học sinh và điểm số tương ứng của học sinh lớp #.
  
## Hỗ trợ
Nếu bạn gặp bất kỳ lỗi nào khi chạy chương trình vui lòng cho tôi biết qua địa chỉ email:....

## Tác giả
- [Nguyen Hong]

---
**Chú ý:** Đảm bảo rằng bạn đã xác định các thông tin cá nhân và tên tác giả thay thế trong tệp README này.
