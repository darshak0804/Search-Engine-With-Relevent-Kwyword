import re
list = ["Think and Grow Rich by Napoleon Hill",
"The 5 Second Rule Transform your Life, Work, and Confidence with Everyday Courage",
"A Brief History of Time: From the Big Bang to Black Holes",
"Who Moved my Cheese: An amazing way to Deal with the Change in Life",
"How to win friends and influence people",
"You can Win: Shiv Khera", "python is a good is of is lang", "python python python", "is python python"]

print("orignallist",str(list))
user_word = input("Search:-")

def searching(mainlist,search_1):
    res = [x for x in mainlist if re.search(search_1,x)]
    print(f"your search result : - {str(res)}")

searching(list,user_word)
