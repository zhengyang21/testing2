def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67, 32)")

def get_user_input():
    temp = input("Enter the temperatures : ")
    temp = temp.split(",")
    for i in range(len(temp)):
        temp[i] = float(temp[i])
    return temp
def calc_average_temperature(temp):
    sum_temp=sum(temp)
    avg=sum_temp/len(temp)
    return avg

def calc_min_max_temperature(temp):
    max=temp[1]
    min=temp[1]
    for i in range(len(temp)):
        if temp[i]>max:
            max=temp[i]
        if temp[i]<min:
            min=temp[i]

    return min,max


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    temp=get_user_input()
    print("The temperatures are" , temp)
    avg=calc_average_temperature(temp)
    print("The average temperatures is" ,avg)
    min, max = calc_min_max_temperature(temp)
    print("max = ",max)
    print("min = ",min)

if __name__ == "__main__":
    main()