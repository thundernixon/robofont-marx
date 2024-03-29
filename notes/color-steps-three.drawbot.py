W, H = 1000, 1000
newPage(W,H)
iterations = 30

start = (0.25, 1, 1, 0.5)
middle = (0, 0.75, 0.35, 0.75)
end = (0, 0, 0.25, 1)

def interp(a,b,f):
    return a+f*(b-a)

transform

for step in range(0,iterations): 
    f = step / iterations
    
    if f < 0.5:
        f = step / (iterations / 2)
        
        print(f)
        fill(interp(start[0],middle[0],f), interp(start[1],middle[1],f), interp(start[2],middle[2],f), interp(start[3],middle[3],f))
    else:
        f = (step - iterations/2) / (iterations/2)
        fill(interp(middle[0],end[0],f), interp(middle[1],end[1],f), interp(middle[2],end[2],f), interp(middle[3],end[3],f))

    rect(0,H/iterations*(iterations-step-1),W, H/iterations)

