def main(problems, solve=False):
    goahead = True
    for num in problems:
        firstnumber = num.split()[0]
        secondnumber = num.split()[2]
        try:
            test = int(firstnumber) + int(secondnumber)
        except:
            goahead = False
            break
    if len(problems)>5:
        print('Error too many problems!!')
    elif goahead == False:
        print('Number can  only contain digits.')
    else:
        num1 = ''
        num2 = ''
        dash = ''
        sumx = ''
        string = ''
        for problem in problems:
            firstnumber = problem.split()[0]
            operator = problem.split()[1]
            secondnumber = problem.split()[2]
            if len(firstnumber) >= 5 or len(secondnumber) >= 5:
                print('The length digits invalid')
            if operator == '+':
                soln = str(int(firstnumber) + int(secondnumber))
            elif operator == '-':
                soln = str(int(firstnumber) - int(secondnumber))
            elif operator != '+' or operator != '-':
                print('The', operator,' is not valid for this problem.\nThe operator should contain "+" or "-".')
                break
            length = max(len(firstnumber), len(secondnumber)) + 2
            top = str(firstnumber).rjust(length)
            bottom = operator + str(secondnumber).rjust(length - 1)
            line = ''
            result = str(soln).rjust(length)
            for s in range(length):
                line += '-'
            if problem != problems[-1]:
                num1 += top + '  '
                num2 += bottom + '  '
                dash += line + '  '
                sumx += result + '  '
            else:
                num1 += top 
                num2 += bottom 
                dash += line
                sumx += result
        if solve == True:
            string = num1 + '\n' + num2 + '\n' + dash + '\n' + sumx
        else:
            string = num1 + '\n' + num2 + '\n' + dash
        print(string)
main(['249 + 3' , '21 + 393', '1 - 859', '1283 + 585' ], True)