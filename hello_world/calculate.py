# 入力された５つの数字の平均を計算し、表示する
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers) 

# main関数
def main():
    # ユーザーから5つの数字を入力してもらう
    numbers = []
    for i in range(5):
        while True:
            try:
                num = float(input(f"数字 {i + 1} を入力してください: "))
                numbers.append(num)
                break
            except ValueError:
                print("無効な入力です。数字を入力してください。")

    # 平均を計算aaaccc
    average = calculate_average(numbers)

    # 結果を表示
    print(f"入力された数字の平均は: {average}")
if __name__ == "__main__":
    main()