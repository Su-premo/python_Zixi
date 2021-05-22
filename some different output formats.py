# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) # 500
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500)) # +500
print("{0: >+10}".format(-500)) # -500
# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다 콤마 찍기
print("{0:,}".format(100000000000))
# 3자리마다 콤마 찍고, +- 부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))
# 3자리마다 콤마 찍고, 부호 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(10000000000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수까지만 표시 (소수점 두째자리까지 = 소수점 셋째자리에서 반올림)
print("{0:.2f}".format(5/3))