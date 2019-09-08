BuildingDict = {
        "mosher":{"spider man": "066",
        "doctor strange": "123",
        "peter quill": "234",
        "iron man": "066",
        "incredible hulk": "456",
        "black widow": "090",
        "hawk eye": "270"
}
}


userNameInput = input("Please enter your name: ")
userRoomInput = str(input("Please enter your room number: "))
userBuildingInput = str(input("Please enter your hall building name: "))

userNameInput = str.lower(userNameInput)
userBuildingInput = str.lower(userBuildingInput)

if userBuildingInput in BuildingDict:
    if userNameInput in BuildingDict["mosher"]:
        if userRoomInput == BuildingDict["mosher"][userNameInput]:
            print("true")
        else:
            print("false")
