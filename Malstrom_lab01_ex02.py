'''
Richard Malstrom
MECH 4100 - Fall 2026
Lab 01 - Python Introduction/Review
Exercise 02
Last modified: 09.08.2026
'''

setpoints = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
feedback = [ 0.0, 5.0, 12.0, 9.8, 10.1, 10.0]
errorList = []

def analyze_control_error(setpoints, feedback_values):
    for i in range(len(setpoints)):
        errorList.append(setpoints[i] - feedback_values[i])
    x = 0
    for i in range(len(errorList)):
            if errorList[i] <= (setpoints[i] * 0.05):
                x = x+1
    return(max(errorList), x, sum(errorList))


max, settled, integral = analyze_control_error(setpoints, feedback)
print("Max Absolute Error: ", max)
print("Settled Count: ", settled)
print("Integral Error: ", integral)

