import matplotlib
import matplotlib.pyplot as plt

max guess 300

g = 9.780
def result (angle):
    if(angle < 0):
        angle = 0
    if(angle > 180):
        angle = 180
    if(angle <= 90):
        multipler = g/90
        return angle * multipler
    else:
        multipler = g/90
        angle = angle - 90
        return -(angle*multipler)

def get_score(data,expectet_data):
    score = result(data)
    score_percent = (abs(score)/expectet_data)*100
    return score_percent


