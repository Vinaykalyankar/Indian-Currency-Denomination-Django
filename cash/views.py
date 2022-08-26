from django.shortcuts import render

def deno(request, in1 = 0,in2 = 0,in3 = 0,in4 = 0,in5 = 0,in6 = 0,in7 = 0, result1 = 0, result2 = 0, result3 = 0,result4 = 0,result5 = 0,result6 = 0,result7 = 0, Total = 0 ):
   if request.method == 'POST':

        in1 = request.POST['inp1']
        in2 = request.POST['inp2']
        in3 = request.POST['inp3']
        in4 = request.POST['inp4']
        in5 = request.POST['inp5']
        in6 = request.POST['inp6']
        in7 = request.POST['inp7']

        result1 = 2000 * int(request.POST['inp1'])
        result2 = 500 * int(request.POST['inp2'])
        result3 = 200 * int(request.POST['inp3'])
        result4 = 100 * int(request.POST['inp4'])
        result5 =  50 * int(request.POST['inp5'])
        result6 =  20 * int(request.POST['inp6'])
        result7 =  10 * int(request.POST['inp7'])



        Total = result1 + result2 + result3 + result4 + result5 + result6 + result7

   return render(request, 'web.html', {'in1':in1, 'in2':in2,'in3':in3,'in4':in4,'in5':in5,
   'in6':in6,'in7':in7,'r1': result1,'r2': result2,'r3': result3,'r4': result4,
    'r5': result5, 'r6': result6, 'r7': result7, "Total":Total})
