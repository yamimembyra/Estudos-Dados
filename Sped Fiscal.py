{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b27a8d79-8a00-480c-9e9c-1159eea892c9",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-11-23 14:26:33.027055\n",
      "['C:\\\\SPED\\\\SPED FISCAL\\\\SPED_FISCAL_202310_1_004.TXT']\n",
      "2023-11-23 14:26:33.361091\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import glob\n",
    "import datetime\n",
    "\n",
    "print(datetime.datetime.now())\n",
    "\n",
    "data = ''\n",
    "def FormatarData(variavel, num):\n",
    "    global data\n",
    "    data = variavel[num][:2] + '/' + variavel[num][2:4] + '/' + variavel[num][4:]\n",
    "    return data\n",
    "\n",
    "listaArquivos = []\n",
    "listaLinhas = []\n",
    "\n",
    "path_efd = glob.glob('C:\\\\SPED\\\\SPED FISCAL\\\\*.txt')\n",
    "\n",
    "print(path_efd)\n",
    "\n",
    "for i in path_efd:\n",
    "    listaLinhas = []\n",
    "    dictCabecalho = {}\n",
    "    dictLinha = {}\n",
    "\n",
    "    df = open(i,'r', encoding=\"Latin-1\")\n",
    "\n",
    "    for line in df:\n",
    "        if '|0000|' in line:\n",
    "            arq = line.split(\"|\")\n",
    "            FormatarData(arq, 4)\n",
    "            dictCabecalho['DT_INI'] = data\n",
    "            FormatarData(arq, 5)\n",
    "            dictCabecalho['DT_FIN'] = data\n",
    "            dictCabecalho['EMPRESA'] = arq[6]\n",
    "            dictCabecalho['CNPJ'] = arq[7]\n",
    "\n",
    "        elif '|C100|' in line: #Danfes\n",
    "            linha = line.split('|')\n",
    "\n",
    "            dictLinha['REG'] = linha[1]\n",
    "            dictLinha['IND_OPER'] = linha[2]\n",
    "            dictLinha['IND_EMIT'] = linha[3]\n",
    "            dictLinha['COD_PART'] = linha[4]\n",
    "            dictLinha['COD_MOD'] = linha[5]\n",
    "            dictLinha['COD_SIT '] = linha[6]\n",
    "            dictLinha['SER'] = linha[7]\n",
    "            dictLinha['NUM_DOC'] = linha[8]\n",
    "            dictLinha['CHV_NFE'] = linha[9]\n",
    "            FormatarData(linha, 10)\n",
    "            dictLinha['DT_DOC'] = data\n",
    "            FormatarData(linha, 11)\n",
    "            dictLinha['DT_E_S'] = data\n",
    "            dictLinha['VL_DOC'] = linha[12]\n",
    "            dictLinha['VL_BC_ICMS'] = linha[21]\n",
    "            dictLinha['VL_ICMS'] = linha[22]\n",
    "            dictLinha['VL_BC_ICMS_ST'] = linha[23]\n",
    "            dictLinha['VL_ICMS_ST'] = linha[24]\n",
    "            dictLinha['VL_IPI'] = linha[25]\n",
    "            dictLinha['VL_PIS'] = linha[26]\n",
    "            dictLinha['VL_COFINS'] = linha[27]\n",
    "\n",
    "            listaLinhas.append(dictLinha)\n",
    "            dictLinha = {}\n",
    "            \n",
    "        elif '|C500|' in line: #Energia Elétrica\n",
    "            linha = line.split('|')\n",
    "\n",
    "            dictLinha['REG'] = linha[1]\n",
    "            dictLinha['IND_OPER'] = linha[2]\n",
    "            dictLinha['IND_EMIT'] = linha[3]\n",
    "            dictLinha['COD_PART'] = linha[4]\n",
    "            dictLinha['COD_MOD'] = linha[5]\n",
    "            dictLinha['COD_SIT '] = linha[6]\n",
    "            dictLinha['SER'] = linha[7]\n",
    "            dictLinha['NUM_DOC'] = linha[10]\n",
    "            FormatarData(linha, 11)\n",
    "            dictLinha['DT_DOC'] = data\n",
    "            FormatarData(linha, 12)\n",
    "            dictLinha['DT_E_S'] = data\n",
    "            dictLinha['VL_DOC'] = linha[13]\n",
    "            dictLinha['VL_BC_ICMS'] = linha[19]\n",
    "            dictLinha['VL_ICMS'] = linha[20]\n",
    "            dictLinha['VL_BC_ICMS_ST'] = linha[21]\n",
    "            dictLinha['VL_ICMS_ST'] = linha[22]\n",
    "\n",
    "\n",
    "            listaLinhas.append(dictLinha)\n",
    "            dictLinha = {}\n",
    "            \n",
    "       \n",
    "        elif '|E001|' in line:\n",
    "            break\n",
    "\n",
    "    listaArquivos.append({'cabecalho': dictCabecalho, 'linhas': listaLinhas})\n",
    "\n",
    "df = pd.json_normalize(listaArquivos, errors='ignore',record_path= 'linhas',\n",
    "meta=[\n",
    "['cabecalho','DT_INI'],\n",
    "['cabecalho','DT_FIN']])\n",
    "\n",
    "df.to_csv(r'C:\\\\SPED\\\\output\\\\resultfiscalc100.csv', sep=';', encoding='utf-8', index=False)\n",
    "\n",
    "print(datetime.datetime.now())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e31864cc-10ae-4a10-b290-ea836774ddea",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dar uma olhada nesse site aqui: https://cursos.alura.com.br/forum/topico-salvar-arquivo-excel-com-varias-abas-145704"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}