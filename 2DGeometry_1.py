
# Function to find the line passing through two points


def Line2D(R, S):

    a = S[1] - R[1]
    b = R[0] - S[0]
    c = a*(R[0]) + b*(R[1])

    if(b < 0):
        print("The equation of line passing through points is:",
              a, "x - ", b, "y = ", c, "\n")
    else:
        print("The equation of line passing through points is: ",
              a, "x + ", b, "y = ", c, "\n")


# Test code
if __name__ == '__main__':
    R = [7, 3]
    S = [4, 1]
    Line2D(R, S)