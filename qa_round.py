from playwright.sync_api import sync_playwright
from pathlib import Path
import json
R=Path('/mnt/data/meu_primeiro_laboratorio_v3')
html=(R/'index.html').read_text()
results=[]
def check(name,success):
 results.append((name,bool(success)))
 print(('PASS ' if success else 'FAIL ')+name)
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=browser.new_page(accept_downloads=True)
 page.goto('about:blank')
 page.evaluate('''window.qaMap=new Map();Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>qaMap.get(k)||null,setItem:(k,v)=>qaMap.set(k,String(v)),removeItem:k=>qaMap.delete(k)}})''')
 page.set_content(html,wait_until='load')
 page.locator('#acceptCheck').check();page.locator('#acceptBtn').click()
 page.locator('#saveBtn').click()
 for i in range(10):
  correct=page.evaluate('state.question.correct')
  page.locator('#choices .choice').nth(correct).click()
  page.locator('#nextBtn').click()
 check('Rodada de 10 respostas completas',page.locator('#quizEnd').is_visible())
 check('Missão marcada como concluída',page.evaluate('state.done.has(0)'))
 check('10 respostas contabilizadas',page.evaluate('state.performance[0].total===10 && state.performance[0].correct===10'))
 check('Persistência opt-in em localStorage',page.evaluate("JSON.parse(localStorage.getItem('mplm_progress_v3')).done.includes(0)"))
 with page.expect_download() as download_event:page.locator('#exportBtn').click()
 download=download_event.value
 temp=R/'qa_progress_export.json';download.save_as(temp)
 payload=json.loads(temp.read_text())
 check('Exportação JSON versão 3 válida',payload['schema']==3 and payload['performance']['0']['total']==10)
 page.on('dialog',lambda dialog:dialog.accept())
 page.locator('#resetBtn').click()
 check('Reiniciar apaga conquistas e métricas',page.evaluate('state.done.size===0 && Object.keys(state.performance).length===0'))
 check('Reiniciar limpa armazenamento antigo e atual',page.evaluate("!localStorage.getItem('mplm_progress_v3') && !localStorage.getItem('mplm_progress_v2')"))
 page.locator('#importFile').set_input_files(str(temp))
 page.wait_for_timeout(350)
 check('Importação JSON recupera a conclusão',page.evaluate('state.done.has(0)'))
 check('Importação recupera métricas matemáticas',page.evaluate('state.performance[0].correct===10'))
 check('Importação respeita opt-in de salvamento',page.evaluate("!localStorage.getItem('mplm_progress_v3')"))
 page.locator('#saveBtn').click()
 check('Salvamento após importação',page.evaluate("JSON.parse(localStorage.getItem('mplm_progress_v3')).performance['0'].total===10"))
 page.set_content(html,wait_until='load')
 check('Reabertura simulada recupera o progresso',page.evaluate('state.done.has(0) && state.save===true'))
 check('Aceite v3 mantido na reabertura simulada',page.locator('#acceptModal').evaluate('el=>!el.open'))
 browser.close()
output={'passed':sum(flag for _,flag in results),'total':len(results),'tests':[{'name':name,'passed':flag} for name,flag in results]}
(R/'qa_round_result.json').write_text(json.dumps(output,ensure_ascii=False,indent=2))
print(output['passed'],'/',output['total'])
raise SystemExit(0 if output['passed']==output['total'] else 1)
