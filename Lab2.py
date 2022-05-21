def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67, 32)")

def get_user_input():
    temp=input("Enter the temperatures : ")
    temp=temp.split(",")
    for i in range(len(temp)):
        temp[i]=float(temp[i])
    return temp

def calc_average_temperature(temp):
    total=0
    for i in range(len(temp)):
        total+=temp[i]
    avg=total/len(temp)
    return avg

def calc_min_max_temperature(temp):
    max=temp[0]
    min=temp[0]
    for i in range(1,len(temp)):
        if temp[i]>max :
            max=temp[i]
        if temp[i]<min :
            min=temp[i]
    return max,min

def main():
    display_main_menu()
    temp=get_user_input()
    print("The temperatures are" , temp)
    avg=calc_average_temperature(temp)
    print("The average temperatures is",avg)
    max,min=calc_min_max_temperature(temp)
    print("Max =",max)
    print("MIn =",min)

if __name__ == "__main__":
    main()