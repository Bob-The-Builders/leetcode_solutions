class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
      closest_point_distance = -1
      counter = 0
      closest_point_index = -1
      for i in points:
        if i[0] == x or i[1] == y:
           distance = abs(x - i[0]) + abs(y - i[0])
           if distance > closest_point_distance:
              closest_point_distance = distance
              closest_point_index = counter
        counter += 1
      print(closest_point_index)
           
Solution().nearestValidPoint(1, 1, [[1,1], [1,1]])