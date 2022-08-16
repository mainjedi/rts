

class RTS:

	def aboveBelow(self, unsortedList, comparator):
		abMapping = { "above": 0, "below": 0}

		for x in unsortedList:
			if x > comparator:
				abMapping["above"]+= 1
			elif x < comparator:
				abMapping["below"] += 1
	
		return abMapping



	def stringRotation(self, inputStr, numRotations):

		inputArr = list(inputStr)
		while numRotations > 0:

			lastChar = inputArr[len(inputArr) - 1]
			toUpdate = inputArr[0]
			for i in range(1, len(inputArr)):
				# swap
				original = inputArr[i]
				inputArr[i] = toUpdate
				toUpdate = original


			inputArr[0] = lastChar
			numRotations -= 1


		return ''.join(inputArr)



# TEST

rts = RTS()
aboveBelowTest = rts.aboveBelow([1,5,2,1,10], 6)
print(aboveBelowTest["above"] == 1)
print(aboveBelowTest["below"] == 4)



stringRotationTest = rts.stringRotation("MyString", 2)
print(stringRotationTest)

print(stringRotationTest == "ngMyStri")

