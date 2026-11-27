import math

def softmax(scores: list[float]) -> list[float]:
  max_score = max(scores)
  expo = [math.exp(n - max_score) for n in scores]
  total = sum(expo)
  return [val / total for val in expo]