import sys
def loanTable(argv):
        loanAmount = float(argv[1])
        annualInterestRate = float(argv[2])
        monthlyPayment = float(argv[3])

        month = 1
        startingBalance = loanAmount
        payment = monthlyPayment
        middleBalance = loanAmount - payment
        interest = middleBalance * annualInterestRate/12/100
        endingBalance = middleBalance + interest

        fileOut = open("output.html", "a")
            
        fileOut.write('''
        <table border=1>
        <tr>
            <th>Month</th>
            <th>Starting Balance</th>
            <th>Payment</th>
            <th>Middle Balance</th>
            <th>Interest</th>
            <th>Ending Balance</th>
        </tr>
        ''')
              
        while startingBalance > 0:
            fileOut.write('<tr><td>'+str(month)+'</td>' +
                          '<td>'+str("%.2f" % startingBalance)+'</td>' +
                          '<td>'+str("%.2f" % payment)+'</td>' +
                          '<td>'+str("%.2f" % middleBalance)+'</td>' + 
                          '<td>'+str("%.2f" % interest)+'</td>' + 
                          '<td>'+str("%.2f" % endingBalance)+'</td></tr>\n')
            
            month+=1
            startingBalance = endingBalance
            
            if endingBalance > monthlyPayment:
                payment = monthlyPayment
            else: payment = endingBalance
            
            middleBalance =  startingBalance - payment
            interest = middleBalance * annualInterestRate/12/100
            endingBalance = middleBalance + interest

        fileOut.write('</table>')
    
        
        
            
if __name__ == "__main__":
    loanTable(sys.argv)