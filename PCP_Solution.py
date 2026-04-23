# ---------------- DATA ----------------
movies = [
    {"title": "Inception", "year": 2010, "rating": 9},
    {"title": "Titanic", "year": 1997, "rating": 8},
    {"title": "Avengers", "year": 2012, "rating": 7},
    {"title": "Interstellar", "year": 2014, "rating": 9},
    {"title": "Joker", "year": 2019, "rating": 8},

    {"title": "Frozen", "year": 2013, "rating": 6},
    {"title": "Batman", "year": 2008, "rating": 9},
    {"title": "Superman", "year": 2013, "rating": 7},
    {"title": "Spiderman", "year": 2021, "rating": 8},
    {"title": "Avatar", "year": 2009, "rating": 9}
]
# Rating: 9 = Excellent, 8 = Good, 7 = Average, 6 = Basic


# ---------------- 1. SEARCH MOVIE ----------------
def find_movie(title):
    for m in movies:
        if m["title"].lower() == title.lower():
            return m
    return "Movie Not Found"


# ---------------- 2. SORT BY YEAR ----------------
def arrange_by_year():
    arr = movies[:]

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j]["year"] > arr[j+1]["year"]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# ---------------- 3. SORT BY RATING ----------------
def arrange_by_rating():
    arr = movies[:]

    for i in range(len(arr)):
        max_idx = i
        for j in range(i+1, len(arr)):
            if arr[j]["rating"] > arr[max_idx]["rating"]:
                max_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr


# ---------------- 4. RECOMMENDATION SYSTEM (MERGE SORT) ----------------
def build_recommendation(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = build_recommendation(arr[:mid])
    right = build_recommendation(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # Higher rating first, if equal → latest year first
        if left[i]["rating"] > right[j]["rating"] or \
           (left[i]["rating"] == right[j]["rating"] and left[i]["year"] > right[j]["year"]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ---------------- 5. SEARCH RATING ----------------
def find_rating(target):
    arr = []

    for m in movies:
        arr.append(m["rating"])

    # Insertion Sort
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    # Binary Search
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return "Rating Found"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return "Rating Not Found"


# ---------------- MENU ----------------
while True:
    print("\n===== 🎬 SMART MOVIE EXPLORER =====")
    print("1. Search Movie")
    print("2. Arrange Movies by Year")
    print("3. Arrange Movies by Rating")
    print("4. Get Recommended Movies")
    print("5. Search Rating")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter movie title: ")
        print(find_movie(title))

    elif choice == "2":
        print(arrange_by_year())

    elif choice == "3":
        print(arrange_by_rating())

    elif choice == "4":
        print(build_recommendation(movies))

    elif choice == "5":
        target = int(input("Enter rating (6-9): "))
        print(find_rating(target))

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")