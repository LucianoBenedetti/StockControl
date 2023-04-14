import pandas as pd
import openpyxl #excel



datos = pd.read_csv('items.csv', header=None)
dataBase =  pd.read_csv('DataBase.DB')

resultado = pd.DataFrame({  'BARCODE': pd.Series(dtype='int'),
                            'ITEMS': pd.Series(dtype='str'),
                            'CUANTITY_UNIT': pd.Series(dtype='int'),
                            'CUANTITY_CTN': pd.Series(dtype='int')})


#print(resultado.dtypes)
#print(dataBase)
for index, row in datos.iterrows():
    barcode = row[2]    #barcode
    count=row[3]        #how many items
    Type='NONE'
    #print(f"{barcode} {count}")

    ##### --------------------------BUSCO ITEM EN BASE DE DATOS-----------------------------
    if dataBase[ dataBase['BARCODE']==barcode].empty:  # si no existe, no esta en la base de datos
        producto='NONE'
    else:                                              #existe, remplazon por nombre de producto
        producto=dataBase[ dataBase['BARCODE']==barcode]
        Type=producto['TYPE'].values[0]
        #print(Type)
        producto=producto['ITEMS'].values[0]
        
        #print(producto)

    ###------------------------- ME FIJO SI HAY PRODUCTOS REPETIDOS Y LOS SUMO -------------   
    if resultado[resultado['BARCODE']==barcode].empty:  # si no existe, agrego nueva fila
        if Type == 'CTN':
            count_unit=0
            count_ctn=count
        else:
            count_unit=count
            count_ctn=0

        resultado.loc[len(resultado.index)] = [barcode, producto, count_unit, count_ctn]   #agrea nueva row a lista
        #print(resultado)        
    
    else:                                               #si exite actualizo
        #print(f"encontro: {resultado[resultado['BARCODE']==barcode]}")
        row_t=resultado[resultado['BARCODE']==barcode]
        if Type == 'CTN':
            count_ctn =row_t['CUANTITY_CTN'].values[0] + count
            count_unit=0
        else:
            count_unit =row_t['CUANTITY_UNIT'].values[0] + count
            count_ctn=0
            #print(total)
        #print(row_t.index)
        resultado.loc[resultado['BARCODE']==barcode] = [barcode,  producto, count_unit, count_ctn]   #actualizo nueva row a lista

print(resultado)
#print(resultado.dtypes)

#resultado.to_csv('resultado.csv', header=True, index=False)
resultado.to_excel('STOCK.xlsx', sheet_name='new_sheet_name')


