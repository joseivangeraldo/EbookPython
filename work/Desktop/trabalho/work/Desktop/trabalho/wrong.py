import graphics
##incorrect way to create two circles

leftEye = Circle(Point(50.0,50.0), 10)
leftEye.setFill('yellow')
leftEye.setOutline('red')
rightEye = leftEye
rightEye.move(20, 0)

# CORRECT WAY USING CLONE METHOD
leftEye = Circle(Point(50.0,50.0), 10)
leftEye.setFill('yellow')
leftEye.setOutline('red')
rightEye = leftEye.clone() #right eye is a copy of the lefteye
rightEye.move(20, 0)
