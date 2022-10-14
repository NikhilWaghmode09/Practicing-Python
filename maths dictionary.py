trignometry={"sin 0":"0", "sin 30":"1/2", "sin 45":"1/√2", "sin 60":"√3/2", "sin 90":"1",
       "sin 120":"√3/2", "sin 225":"-1/√2", "sin 240":"-√3/2", "sin 270":"-1", "sin 315":"-1/√2", "sin 360":"0",
       "cos 0":"1", "cos 30":"√3/2", "cos 45":"1√2", "cos 60":"1/2", "cos 90":"0",
       "cos 120":"-1/2", "cos 225":"-1/√2","cos 240":"-1/2","cos 270":"0","cos 315":"1/√2", "cos 360":"1",
       "tan 0":"0", "tan 30":"1/√3", "tan 45":"1", "tan 60":"√3", "tan 90":"Not defined",
       "tan 120":"-1/√3", "tan 225":"1","tan 240":"√3", "tan 270":"Not defined", "tan 315":"-1", "tan 360":"0",
       "cosec 0":"Not defined", "cosec 30":"2", "cosec 45":"√2", "cosec 60":"2/√3", "cosec 90":"1",
       "cosec 120":"2/√3", "cosec 225":"-√2", "cosec 240":"-2/√3", "cosec 270":"-1", "cosec 315":"-2/√3", "cosec 360":"Not defined",
       "sec 0":"1", "sec 30":"2/√3", "sec 45":"√2", "sec 60":"2", "sec 90":"Not defined",
       "sec 120":"-2", "sec 225":"-√2", "sec 240":"-2", "sec 270":"Not defined", "sec 315":"√2", "sec 360":"1",
       "cot 0":"Not defined", "cot 30":"√3", "cot 45":"1", "cot 60":"1/√3", "cot 90":"0",
       "cot 120":"-√3", "cot 225":"1", "cot 240":"1/√3", "cot 270":"Not defined", "cot 315":"0", "cot 360":"Not defined"}
print("Ask for any trignometric function or any trignometic formula.(Note:-Use '@' instead of 'Θ'.)")
m2={"cos 2@":"cos²@-sin²@, 1-2sin²@, 2cos²@-1, 1-tan²@/1+tan²@","sin 2@":"2sin@cos@, 2tan@/1+tan²@",
    "tan2@":"2tan@/1-tan²@","cos(a+b)":"cos a.cos b - sin a.sin b","cos(a-b)":"sin a.sin b + cos a.cos b",
    "sin(a+b)":"sin a.cos b + sin b.cos a","sin(a-b)":"sin a.cos b - cos a.sin b","tan(a+b)":"tan a + tan b/1-tan a.tan b",
    "tan(a-b)":"tan a - tan b/1+tan a.tan b"}
trignometry.update(m2)
vara=input()
print("This is your answer",trignometry.get(vara.lower()))