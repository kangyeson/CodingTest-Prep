h, m = map(int, input().split())
print(h if m-45 >= 0 else h-1 if m-45 < 0 and h-1>=0 else (h-1)+24,
      m-45 if m-45 >= 0 else (m-45)+60)