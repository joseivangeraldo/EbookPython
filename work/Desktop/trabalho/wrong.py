import graphics


##incorrect way to create two circles

leftEye = Circle(Point(50,50), 10)
leftEye.setFill('yellow')
leftEye.setOutline('red')
rightEye = leftEye
rightEye.move(20, 0)
