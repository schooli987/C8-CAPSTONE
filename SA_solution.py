# ---------------- DATA ----------------
patients = [
    {"name": "Ayaan", "age": 25, "priority": 2},
    {"name": "Zoya", "age": 40, "priority": 1},
    {"name": "Ravi", "age": 30, "priority": 3},
    {"name": "Neha", "age": 50, "priority": 2},
    {"name": "Kabir", "age": 60, "priority": 1},

    {"name": "Meera", "age": 35, "priority": 2},
    {"name": "Arjun", "age": 28, "priority": 3},
    {"name": "Sara", "age": 45, "priority": 1},
    {"name": "Vikram", "age": 55, "priority": 2},
    {"name": "Isha", "age": 22, "priority": 3},

    {"name": "Rahul", "age": 38, "priority": 1},
    {"name": "Ananya", "age": 27, "priority": 2},
    {"name": "Karan", "age": 48, "priority": 3},
    {"name": "Priya", "age": 33, "priority": 2},
    {"name": "Rohit", "age": 41, "priority": 1},

    {"name": "Sneha", "age": 29, "priority": 3},
    {"name": "Aditya", "age": 52, "priority": 2},
    {"name": "Pooja", "age": 36, "priority": 1},
    {"name": "Manish", "age": 44, "priority": 3},
    {"name": "Divya", "age": 31, "priority": 2}
]
# Priority: 1 = Critical, 2 = Moderate, 3 = Stable


# ---------------- 1. SEARCH ----------------
def find_patient(name):
    for p in patients:
        if p["name"].lower() == name.lower():
            return p
    return "Patient Not Found"


# ---------------- 2. SORT BY AGE ----------------
def arrange_by_age():
    arr = patients[:]

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j]["age"] > arr[j+1]["age"]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr


# ---------------- 3. SORT BY PRIORITY ----------------
def arrange_by_priority():
    arr = patients[:]

    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j]["priority"] < arr[min_idx]["priority"]:
                min_idx = j

        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp

    return arr


# ---------------- 5. SEARCH PRIORITY ----------------
def find_priority(target):
    arr = []

    for p in patients:
        arr.append(p["priority"])

    # sort internally
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    # search
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return "Priority Found"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return "Priority Not Found"
#----------------- 5. EMERGENCY QUEUE----------------------

def build_emergency_queue(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = build_emergency_queue(arr[:mid])
    right = build_emergency_queue(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["priority"] < right[j]["priority"] or \
           (left[i]["priority"] == right[j]["priority"] and left[i]["age"] > right[j]["age"]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# ---------------- MENU ----------------
while True:
    print("\n===== 🚑 HOSPITAL EMERGENCY MENU =====")
    print("1. Search Patient")
    print("2. Arrange Patients by Age")
    print("3. Arrange Patients by Priority")
    print("4. Search Priority")
    print("5. Emergency Queue")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter patient name: ")
        print(find_patient(name))

    elif choice == "2":
        print(arrange_by_age())

    elif choice == "3":
        print(arrange_by_priority())

    elif choice == "4":
        target = int(input("Enter priority (1-3): "))
        print(find_priority(target))

    elif choice=="5":
        print(build_emergency_queue(patients))

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")



