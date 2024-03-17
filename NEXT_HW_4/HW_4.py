maximum = int(input("숫자게임의 최댓값을 입력해주세요::"))
low = 1

input(f"1부터 {maximum}까지의 숫자를 하나 생각하세요\n준비가 되었으면 ENTER를 누르세요")

count = 0
while True:
    count += 1
    mid = (low + maximum) // 2
    feedback = input(f"당신이 생각한 숫자는 {mid} 입니까?\n맞으면 '맞음' 더 크다면 '큼' 더 작으면 '작음'을 입력해주세요")
    if feedback == '맞음' :
        print(f"{count}번만에 맞췄다!")
        break
    elif feedback == '작음':

        maximum = mid -1
    else :
        low = mid + 1