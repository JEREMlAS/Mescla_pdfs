import PyPDF2 as pyf 
from pathlib import Path

pdf_mesclado = pyf.PdfMerger()

pdf_1 = input('pdf principal/primeiro: ')
pdf_mesclado.append(pdf_1)

pdf_2 = input('segundo pdf: ')

posicao = input('posicao [final/inicial]: ')
if posicao == 'inicial':
    pdf_mesclado.merge(0, pdf_2)
elif posicao == 'final':
    pdf_mesclado.append(pdf_2)
else: 
    print('Opção inválida')


nome = input('Nome do arquivo final: ')
with Path(f'{nome}.pdf').open(mode='wb') as arquivo:
    pdf_mesclado.write(arquivo)
