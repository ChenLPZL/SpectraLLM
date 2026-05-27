import math


def euler_e(terms=20):
    """Euler's number e via Taylor series: e = sum(1/k! for k=0..inf)"""
    e = 0.0
    factorial = 1
    for k in range(terms):
        e += 1.0 / factorial
        factorial *= (k + 1)
    return e


def euler_numbers(n):
    """
    Euler zigzag numbers (secant/tangent numbers).
    E_0=1, E_1=1, E_2=1, E_3=2, E_4=5, E_5=16, ...
    Recurrence: 2 * E_{n+1} = sum_{k=0..n} C(n,k) * E_k * E_{n-k}
    """
    E = [0] * (n + 1)
    E[0] = 1
    if n >= 1:
        E[1] = 1

    for m in range(1, n):
        total = sum(math.comb(m, k) * E[k] * E[m - k] for k in range(m + 1))
        E[m + 1] = total // 2

    return E


def euler_totient(n):
    """Euler's totient function phi(n): count of k in [1,n] coprime to n."""
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


# ===== Test cases =====
if __name__ == "__main__":
    print("=" * 50)
    print("1. Euler's Number e (Taylor series)")
    print("=" * 50)
    e_val = euler_e(terms=20)
    print(f"  Computed e = {e_val:.15f}")
    print(f"  Expected e = {math.e:.15f}")
    print(f"  Difference = {abs(e_val - math.e):.2e}")
    print(f"  PASS: {abs(e_val - math.e) < 1e-14}")

    print("\n" + "=" * 50)
    print("2. Euler Zigzag Numbers (E_0 to E_10)")
    print("=" * 50)
    expected_zigzag = [1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936, 50521]
    E = euler_numbers(10)
    for i in range(11):
        status = "PASS" if E[i] == expected_zigzag[i] else "FAIL"
        print(f"  E_{i} = {E[i]} (expected {expected_zigzag[i]}) {status}")

    print("\n" + "=" * 50)
    print("3. Euler's Totient Function phi(n)")
    print("=" * 50)
    totient_tests = [
        (1, 1), (2, 1), (3, 2), (4, 2), (5, 4),
        (6, 2), (7, 6), (8, 4), (9, 6), (10, 4),
        (12, 4), (36, 12), (97, 96), (100, 40),
    ]
    all_pass = True
    for n, expected in totient_tests:
        result = euler_totient(n)
        passed = result == expected
        if not passed:
            all_pass = False
        status = "PASS" if passed else "FAIL"
        print(f"  phi({n:>3}) = {result:>3} (expected {expected:>3}) {status}")

    print(f"\n  Totient tests: {'All passed!' if all_pass else 'Some FAILED!'}")
