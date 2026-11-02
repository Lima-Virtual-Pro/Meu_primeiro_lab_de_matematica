"""Independent verification of generated answer keys from problem text; Python is only QA, app runs in JS without it."""
from fractions import Fraction
from pathlib import Path
import json,re,subprocess
R=Path('/mnt/data/meu_primeiro_laboratorio_v3')
script='''const fs=require('fs'),vm=require('vm');let ctx={window:{},document:{addEventListener(){}}};vm.createContext(ctx);vm.runInContext(fs.readFileSync(process.argv[1],'utf8'),ctx); process.stdout.write(vm.runInContext('JSON.stringify({course:COURSE,bank:BANK})',ctx));'''
data=json.loads(subprocess.run(['node','-e',script,str(R/'app.js')],capture_output=True,text=True,check=True).stdout)
(R/'banco_questoes_2400.json').write_text(json.dumps(data,ensure_ascii=False,indent=1))

def nums(x):return list(map(int,re.findall(r'\d+',x)))
def fnum(v):return Fraction(v)
def format_frac(fr):return str(fr.numerator) if fr.denominator==1 else f'{fr.numerator}/{fr.denominator}'
def calc(t,q):
 n=nums(q)
 if t==0:return f'{n[1]}/{n[0]}'
 if t==1:return str(n[0] if 'numerador' in q else n[1])
 if t==2:return Fraction(n[0],n[1])
 if t==3:return format_frac(Fraction(n[0],n[1]))
 if t==4:return f'{max(n[0],n[2])}/{n[1]}'
 if t==5:return '>' if n[0]*n[3]>n[2]*n[1] else '<' if n[0]*n[3]<n[2]*n[1] else '='
 if t in (6,7):return format_frac(Fraction(n[0],n[1])+Fraction(n[2],n[3]))
 if t in (8,9):return format_frac(Fraction(n[0],n[1])-Fraction(n[2],n[3]))
 if t==10:return format_frac(Fraction(n[0],n[1])*Fraction(n[2],n[3]))
 if t==11:return format_frac(Fraction(n[0],n[1])/Fraction(n[2],n[3]))
 if t==12:return int(n[0]*n[1]/n[2])
 if t==13:
  whole,rem=divmod(n[0],n[1]);return f'{whole} {rem}/{n[1]}'
 if t==14:return f'{n[0]*100/n[1]:g}%'
 if t==15:return f'{n[3]}/{n[2]}'  # n0=0, n1=1, n2=interval count, n3=mark
 if t==16:return n[0]+n[1] if 'recebeu' in q else n[0]-n[1]
 if t==17:return n[0]*n[1]
 if t==18:return n[0]//n[1]
 if t==19:
  x=list(map(int,re.findall(r'(?<!\d)\d+(?!\d)',q)))
  return x[3]+(x[1]-x[0])
 if t==20:return n[0]*100 if 'Quantos centímetros' in q else n[0]//100
 if t==21:return f'{2*(n[0]+n[1])} m'
 if t==22:return f'{n[0]*n[1]} cm²'
 if t==23:return n[0]-n[1]*n[2] if 'sobrará' in q else n[0]*n[1]
 raise ValueError(t)
issues=[]
for li,lesson in enumerate(data['course']):
 bank=data['bank'][li]
 if len(bank)!=100:issues.append([li,'bank size',len(bank)])
 if len({q['q'] for q in bank})!=len(bank):issues.append([li,'duplicate'])
 for j,item in enumerate(bank):
  try:
   correct=item['choices'][item['correct']]
   actual=calc(lesson['type'],item['q'])
   if lesson['type']==2:
    if Fraction(correct)!=actual:issues.append([li,j,item['q'],str(correct),str(actual)])
   elif str(correct)!=str(actual):issues.append([li,j,item['q'],str(correct),str(actual)])
   if len(item['choices'])!=4 or len(set(item['choices']))!=4:issues.append([li,j,'choices'])
   if not item['explanation'] or not item['hint']:issues.append([li,j,'missing feedback'])
  except Exception as e:issues.append([li,j,type(e).__name__,str(e),item['q']])
print('TOTAL',sum(len(x) for x in data['bank']),'ISSUES',len(issues));print('FIRST',issues[:20]);
(R/'qa_math_result.json').write_text(json.dumps({'total':2400,'issues':issues[:100],'issue_count':len(issues)},ensure_ascii=False,indent=2))
raise SystemExit(1 if issues else 0)
