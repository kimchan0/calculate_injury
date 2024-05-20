def calculate_injury_rate():
    while True:
        try:
            total_workers = int(input("연평균 근로자 수 : "))
            total_injuries = int(input("연간 재해자 수 : "))
            if total_workers <= 0 or total_injuries < 0:
                raise ValueError("연평균 근로자 자 수는 0보다 커야 하며 연간 재해자 수는 음수가 아니어야 합니다.")
            break
        except ValueError as e:
            print(f"입력이 잘못 되었습니다.{e}. 다시 시도해 주세요.")

    injury_rate = (total_injuries / total_workers) * 100

    print(f"연천인율: {injury_rate:.2f}%")

if __name__ == "__main__":
    calculate_injury_rate()