#!/usr/bin/python
import unittest

def calculateWaterAmt(l, r, arr):
    filled_amt = 0
    for i in arr[l+1:r]:
        filled_amt += i

    totalArea = min(arr[l], arr[r]) * (abs(l - r) - 1)
    print(filled_amt, totalArea, totalArea-filled_amt, l, r, arr)
    return totalArea - filled_amt

def getWaterFill(arr):
    amt = 0
    if len(arr) <= 2:
        return amt

    curr = 1
    l = curr - 1
    r = curr + 1
    # continue until r is the last element of the list
    while r < len(arr):
        # is R the last elemnet on the list? 
        if r == len(arr)-1:
            # is elem at r and l greater than curr? 
            if arr[r] > arr[curr] and arr[l] >= arr[curr]:
                amt += calculateWaterAmt(l, r, arr)
                return amt
            else:
                return amt
        else:
            # is elem at l greater than curr? 
            if arr[l] > arr[curr]:
                # is eleem at r greater than curr and r + 1 ? 
                if arr[r] > arr[curr] and arr[r] > arr[r+1]:
                    # calculate amt
                    amt += calculateWaterAmt(l, r, arr)
                    # shift l, curr, and r
                    l = r
                    curr = l + 1
                    r = l + 2
                else:
                    # shift curr and r 
                    curr = curr + 1
                    r = r + 1
            else:
                # shift l, curr, and r
                l = curr
                curr = l + 1
                r = curr + 1
        
    return amt

class WaterFillTest(unittest.TestCase):
  def test(self):
      arr = [0,1,2,1,0]
      self.assertEqual(getWaterFill(arr), 0)
      arr2 = [0,3,1,2,3,0]
      self.assertEqual(getWaterFill(arr2), 3)
      arr3 = [0,2,1,2,1,2,0]
      self.assertEqual(getWaterFill(arr3), 2)
      arr4 = [0,3,1,2,1,4,0,3,0] 
      self.assertEqual(getWaterFill(arr4), 5)


if __name__ == '__main__':
    unittest.main()