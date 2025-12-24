import itertools

def solve_lab():
    # 1. Список всех предметов (название, символ, размер, ценность)
    items = [
        ("rifle", 'r', 3, 25), ("pistol", 'p', 2, 15),
        ("ammo", 'a', 2, 15), ("medkit", 'm', 2, 20),
        ("inhaler", 'i', 1, 5), ("knife", 'k', 1, 15),
        ("axe", 'x', 3, 20), ("talisman", 't', 1, 25),
        ("flask", 'f', 1, 15), ("antidot", 'd', 1, 10),
        ("supplies", 's', 2, 20), ("crossbow", 'c', 2, 20)
    ]
    
    total_value_all = sum(item[3] for item in items)  # 205
    initial_points = 15
    
    # Функция для расчета итоговых очков выживания
    def calculate_final_score(taken_value):
        points_left = total_value_all - taken_value
        return initial_points + taken_value - points_left

    # --- ЗАДАЧА 1: ОСНОВНОЕ РЕШЕНИЕ (3x3 = 9 ячеек) ---
    print("=== ОСНОВНОЕ ЗАДАНИЕ (Инвентарь 3x3) ===")
    capacity_9 = 9
    n = len(items)
    dp = [[0 for _ in range(capacity_9 + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity_9 + 1):
            if items[i-1][2] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-items[i-1][2]] + items[i-1][3])
            else:
                dp[i][w] = dp[i-1][w]

    # Обратный ход (поиск предметов)
    res_v, cur_w = dp[n][capacity_9], capacity_9
    taken_9 = []
    for i in range(n, 0, -1):
        if res_v != dp[i-1][cur_w]:
            taken_9.append(items[i-1])
            res_v -= items[i-1][3]
            cur_w -= items[i-1][2]

    # Вывод сетки
    grid = []
    for it in taken_9: grid.extend([f"[{it[1]}]"] * it[2])
    while len(grid) < 9: grid.append("[ ]")
    for i in range(0, 9, 3): print(",".join(grid[i:i+3]))
    
    final_score_9 = calculate_final_score(dp[n][capacity_9])
    print(f"Итоговые очки: {final_score_9}\n")


    # --- ЗАДАЧА 2: ДОПЗАДАНИЕ (7 ячеек) ---
    print("=== ДОПЗАДАНИЕ (Инвентарь 7 ячеек) ===")
    capacity_7 = 7
    # Найдем максимум для 7 ячеек через DP
    dp7 = [0] * (capacity_7 + 1)
    for _, _, w, v in items:
        for j in range(capacity_7, w - 1, -1):
            dp7[j] = max(dp7[j], dp7[j-w] + v)
    
    max_v7 = dp7[capacity_7]
    final_score_7 = calculate_final_score(max_v7)
    
    print(f"Макс. ценность предметов для 7 ячеек: {max_v7}")
    print(f"Итоговые очки: {final_score_7}")
    if final_score_7 <= 0:
        print("ВЫВОД: Решения для 7 ячеек не существует, так как макс. счет не больше 0.\n")


    # --- ЗАДАЧА 3: ВСЕ КОМБИНАЦИИ ДЛЯ 3x3 (Счет > 0) ---
    print("=== ВСЕ КОМБИНАЦИИ (для 3x3 со счетом > 0) ===")
    valid_combinations = []
    # Перебираем все возможные подмножества предметов
    for r in range(1, len(items) + 1):
        for combo in itertools.combinations(items, r):
            w_sum = sum(it[2] for it in combo)
            v_sum = sum(it[3] for it in combo)
            if w_sum <= 9:
                score = calculate_final_score(v_sum)
                if score > 0:
                    valid_combinations.append(([it[1] for it in combo], score))
    
    print(f"Найдено комбинаций: {len(valid_combinations)}")
    print("Примеры первых 5 комбинаций (символы, итоговый счет):")
    for c, s in valid_combinations[:5]:
        print(f"Предметы: {c} -> Счет: {s}")

solve_lab()