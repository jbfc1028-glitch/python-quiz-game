
import json
import time
import tracemalloc
from pathlib import Path

# 성능 테스트용 파일 (실제 state.json은 변경하지 않음)
TEST_FILE = Path("benchmark_state.json")


def create_quizzes(count):
    return [
        {
            "question": f"테스트 문제 {i}",
            "choices": ["서울", "부산", "대구", "인천"],
            "answer": 1,
        }
        for i in range(count)
    ]


def benchmark(count):
    quizzes = create_quizzes(count)

    tracemalloc.start()

    start = time.perf_counter()
    with open(TEST_FILE, "w", encoding="utf-8") as file:
        json.dump(quizzes, file, ensure_ascii=False, indent=4)
    save_time = time.perf_counter() - start

    start = time.perf_counter()
    with open(TEST_FILE, "r", encoding="utf-8") as file:
        loaded = json.load(file)
    load_time = time.perf_counter() - start

    start = time.perf_counter()
    target = f"테스트 문제 {count - 1}"
    found = next(
        (quiz for quiz in loaded if quiz["question"] == target),
        None,
    )
    search_time = time.perf_counter() - start

    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"\n퀴즈 {count:,}개")
    print(f"저장 시간: {save_time:.6f}초")
    print(f"불러오기 시간: {load_time:.6f}초")
    print(f"검색 시간: {search_time:.6f}초")
    print(f"최대 추적 메모리: {peak_memory / 1024 / 1024:.2f}MB")
    print(f"검색 성공: {found is not None}")


try:
    for count in [100, 1000, 10000]:
        benchmark(count)
finally:
    if TEST_FILE.exists():
        TEST_FILE.unlink()
