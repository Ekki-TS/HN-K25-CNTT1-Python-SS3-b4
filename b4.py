print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")

employee_count = 0

while employee_count <= 0:
    employee_count = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
    if employee_count > 0:
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho "f"{employee_count} nhân sự mới!")
        print("--- CHƯƠNG TRÌNH KẾT THÚC --- ")
    else:
        print("[LỖI] Số lượng không hợp lệ! ""Vui lòng nhập một con số lớn hơn 0.")
