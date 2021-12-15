"""
knapsack_topdown: 배낭 문제 (top-down 방식)
"""

def knapsack(capa,n):
  if capa == 0 or n == 0:
    return 0
  if size[n-1] > capa:
    return knapsack(capa, n-1)
  else:
    return max(value[n-1] + knapsack(capa-size[n-1], n-1), knapsack(capa, n-1))


if __name__ == "__main__":
  size = [1,3,4]
  value = [3,4,5]
  print(knapsack(4,3))