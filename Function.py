import time

class Project:
    def __init__(self, id, name, type, amount, progress, date):
        self.id = id
        self.name = name
        self.type = type
        self.amount = amount
        self.progress = progress
        self.date = date

# 2 Thuật Toán Tìm Kiếm
def Tìm_Kiếm_Tuyến_Tính(projects, key):
    for project in projects:
        if key == project.id:
            return project
    return None

def Tìm_Kiếm_Nhị_Phân(projects, key):
    thấp = 0
    cao = len(projects) - 1
    while thấp <= cao:
        giữa = (thấp + cao) // 2
        if key == projects[giữa].id:
            return projects[giữa]
        elif key < projects[giữa].id:
            cao = giữa - 1
        else:
            thấp = giữa + 1
    return None

# 5 Thuật Toán Sắp Xếp
def Sắp_Xếp_Trao_Đổi(projects, ascending=True):
    start_time = time.time()
    for i in range(len(projects)):
        for j in range(i + 1, len(projects)):
            if (projects[i].id > projects[j].id) == ascending:
                projects[i], projects[j] = projects[j], projects[i]
    end_time = time.time()
    return end_time - start_time

def Sắp_Xếp_Nổi_Bọt(projects, ascending=True):
    start_time = time.time()
    n = len(projects)
    for i in range(n):
        for j in range(0, n-i-1):
            if (projects[j].id > projects[j+1].id) == ascending:
                projects[j], projects[j+1] = projects[j+1], projects[j]
    end_time = time.time()
    return end_time - start_time

def Sắp_Xếp_Chèn(projects, ascending=True):
    start_time = time.time()
    for i in range(1, len(projects)):
        key = projects[i]
        j = i - 1
        while j >= 0 and (key.id < projects[j].id) == ascending:
            projects[j + 1] = projects[j]
            j -= 1
        projects[j + 1] = key
    end_time = time.time()
    return end_time - start_time

def Sắp_Xếp_Chọn(projects, ascending=True):
    start_time = time.time()
    for i in range(len(projects)):
        min_idx = i
        for j in range(i + 1, len(projects)):
            if (projects[j].id < projects[min_idx].id) == ascending:
                min_idx = j
        projects[i], projects[min_idx] = projects[min_idx], projects[i]
    end_time = time.time()
    return end_time - start_time

def Sắp_Xếp_Phân_Hoạch(projects, ascending=True):
    start_time = time.time()
    if len(projects) <= 1:
        end_time = time.time()
        return projects, end_time - start_time
    
    pivot = projects[len(projects) // 2].id
    trái = [project for project in projects if project.id < pivot]
    giữa = [project for project in projects if project.id == pivot]
    phải = [project for project in projects if project.id > pivot]
    
    trái, _ = Sắp_Xếp_Phân_Hoạch(trái, ascending)
    phải, _ = Sắp_Xếp_Phân_Hoạch(phải, ascending)
    
    sorted_projects = trái + giữa + phải
    
    end_time = time.time()
    return sorted_projects, end_time - start_time

def Hiển_Thị(projects):
    for project in projects:
        print(vars(project))

def main():
    projects = []
    while True:
        print("\n1. Thêm Dự Án")
        print("2. Tìm Kiếm Dự Án")
        print("3. Sắp Xếp Dự Án")
        print("4. Hiển Thị Danh Sách")
        print("5. Thoát")

        choice = int(input("Hãy Nhập Số Lựa Chọn 1 -> 5: "))

        if choice == 1:
            id = int(input("Nhập Số ID Dự Án: "))
            name = input("Nhập Tên Dự Án: ")
            project_type = input("Nhập Loại Dự Án: ")
            project_amount = float(input("Nhập Số Lượng Dự Án: "))
            project_progress = float(input("Nhập Tiến Độ Dự Án: "))
            completion_date = input("Nhập Số Ngày Hoàn Thành (dd/mm/yyyy): ")
            project = Project(id, name, project_type, project_amount, project_progress, completion_date)
            projects.append(project)
        elif choice == 2:
            print("1. Tìm Kiếm Tuyến Tính")
            print("2. Tìm Kiếm Nhị Phân")
            search_choice = int(input("Hãy chọn phương pháp tìm kiếm: "))
            if search_choice == 1:
                key = int(input("Nhập ID dự án để tìm kiếm: "))
                result = Tìm_Kiếm_Tuyến_Tính(projects, key)
                if result:
                    print("Đã tìm thấy dự án:")
                    print(vars(result))
                else:
                    print("Dự án không tìm thấy.")
            elif search_choice == 2:
                key = int(input("Nhập ID dự án để tìm kiếm: "))
                result = Tìm_Kiếm_Nhị_Phân(projects, key)
                if result:
                    print("Đã tìm thấy dự án:")
                    print(vars(result))
                else:
                    print("Dự án không tìm thấy.")
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        elif choice == 3:
            print("\n1. Phương pháp Đổi chỗ trực tiếp")
            print("2. Phương pháp Nổi bọt")
            print("3. Phương pháp Chèn trực tiếp")
            print("4. Phương pháp Chọn trực tiếp")
            print("5. Phương pháp dựa trên phân hoạch")
            sort_choice = int(input("Nhập lựa chọn thuật toán sắp xếp: "))
            order_choice = int(input("Chọn thứ tự sắp xếp (1: Tăng dần, 2: Giảm dần): "))
            if sort_choice in range(1, 6):
                if order_choice == 1:
                    ascending = True
                elif order_choice == 2:
                    ascending = False
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
                    continue
                if sort_choice == 1:
                    execution_time = Sắp_Xếp_Trao_Đổi(projects, ascending)
                elif sort_choice == 2:
                    execution_time = Sắp_Xếp_Nổi_Bọt(projects, ascending)
                elif sort_choice == 3:
                    execution_time = Sắp_Xếp_Chèn(projects, ascending)
                elif sort_choice == 4:
                    execution_time = Sắp_Xếp_Chọn(projects, ascending)
                elif sort_choice == 5:
                    sorted_projects, execution_time = Sắp_Xếp_Phân_Hoạch(projects, ascending)
                    print("Dự án được sắp xếp thành công.")
                    print(f"Thời gian thực hiện: {execution_time} giây")
                    print("Danh sách dự án sau khi được sắp xếp:")
                    Hiển_Thị(sorted_projects)
                print("Dự án được sắp xếp thành công.")
                print(f"Thời gian thực hiện: {execution_time} giây")
                # Hiển thị danh sách đã được sắp xếp
                print("Danh sách dự án sau khi được sắp xếp:")
                Hiển_Thị(projects)
        elif choice == 4:
            Hiển_Thị(projects)
        elif choice == 5:
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()