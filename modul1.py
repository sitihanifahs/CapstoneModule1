productData = {
    'S121913' : {'name': 'Lip Sleeping Mask','category': 'Skincare','stock': 40,'price': 382500},
    'S031619' : {'name': 'Clear-C Peeling Serum','category': 'Skincare','stock': 20,'price': 410000},
    'S120105' : {'name': 'Clear-C Advanced Effector EX','category': 'Skincare','stock': 100,'price': 550000},
    'S180300' : {'name': 'Radian-C Cream','category': 'Skincare','stock': 30,'price': 636000},
    'S230413' : {'name': 'White Dew Milky Cleanser','category': 'Skincare','stock': 25,'price': 441000},
    'M140307' : {'name': 'Neo Cushion Glow','category': 'Makeup','stock': 35,'price': 620000},
    'M140607' : {'name': 'Neo Foundation Glow','category': 'Makeup','stock': 45,'price': 620000},
    'M120616' : {'name': 'Light Fit Powder','category': 'Makeup','stock': 50,'price': 671000},
    'M071319' : {'name': 'Glowy Makeup Serum','category': 'Makeup','stock': 55,'price': 518000},
    'M121202' : {'name': 'Layering Lip Bar','category': 'Makeup','stock': 60,'price': 390000}
    }

def mainMenu() :
    while True :
        print('''
        Welcome to LANEIGE Main Menu Product Management Application!
            
            Application Menu List :
            1. Read Product Data
            2. Add Product Data
            3. Update Product Data
            4. Delete Product Data
            5. Exit Application''')    
        mainMenuOption = input('\nPlease input the number of menu you want to run (1/2/3/4/5) : ')
        if (mainMenuOption == '1') :
            readMenu()
            break  
        elif (mainMenuOption == '2') :
            addMenu()
            break
        elif (mainMenuOption == '3') :
            updateMenu()
            break
        elif (mainMenuOption == '4') :
            deleteMenu()
            break
        elif (mainMenuOption == '5') :
            print('\nThank you for using LANEIGE Product Management Application! Have a nice day!\n')
            break
        else :
            print('\nYour input is invalid! Recognized input value : 1/2/3/4/5 !')
            mainMenu()
            break

def readMenu() :
    readMenuOption = input('''
        Welcome to READ Product Data Menu!
         
        Menu Options :
        1. Display Entire Product Data
        2. Display Specific Product Data
        3. Go Back to Main Menu
            
        Please input the number of option you want to run (1/2/3) : ''')       
    if (readMenuOption == '1') :
        displayEntireData()
    elif (readMenuOption == '2') :
        displaySpecificData()
    elif (readMenuOption == '3') :
        mainMenu()
    else :
        print('\nYour input is invalid! Recognized input value : 1/2/3 !')
        readMenu()

def displayEntireData() :
    if (len(productData)>0) :
        allDataTable()
        readMenu()
    else :
        noDataNotif()

def headerTable() :
    print('\n\t\t\t\tLANEIGE PRODUCT')
    print('-'*82)
    print('| Product ID | Product Name\t\t\t| Category\t| Stock\t| Price  |')
    print('-'*82)

def allDataTable() :
    print('\nThe following is a display of all existing data products :')
    headerTable()
    for id in productData :
        print('|',id,'   |',productData[id]['name'],' '*(31-len(productData[id]['name'])),'|',productData[id]['category'],'\t|',productData[id]['stock'],'\t|',productData[id]['price'],'| ')
    print('-'*82)

def noDataNotif() :
    print("\nThere aren't available data to display!")
    readMenu()

def displaySpecificData() :
    if (len(productData)>0) :
        id = input('\nPlease input the specific Product ID to be displayed : ')
        if id in productData.keys() :
            specificDataTable(id)
            readMenu()
        else :
            idNotFound(id)
            readMenu()
    else :
        noDataNotif()

def specificDataTable(id) :
    print('\nThe following is a display of product ID {} data :'.format(id))
    headerTable()
    print('|',id,'   |',productData[id]['name'],' '*(31-len(productData[id]['name'])),'|',productData[id]['category'],'\t|',productData[id]['stock'],'\t|',productData[id]['price'],'| ')
    print('-'*82)

def idNotFound(id) :
    print('\nThe product ID {} not found!'.format(id))
    allDataTable()

def addMenu() :
    addMenuOption = input('''
        Welcome to ADD Product Data Menu!
         
        Menu Options :
        1. Add New Product Data
        2. Go Back to Main Menu
            
        Please input the number of option you want to run (1/2) : ''')   
    if (addMenuOption == '1') :
        addNewData()
    elif (addMenuOption == '2') :
        mainMenu()
    else :
        print('\nYour input is invalid! Recognized input value : 1 or 2 !')
        addMenu()

def addNewData() :
    id = input('\nPlease input the new Product ID : ')
    if id in productData.keys() :
        specificDataTable(id)
        print("\nThe Product ID {} already exists! You can't add a duplicate Product ID!".format(id))
        addMenu()
    else :
        productName = input('Please input the product name : ')
        productCategory = input('Please input the product category : ')
        productStock = int(input('Please input the product stock : '))
        productPrice = int(input('Please input the product price : '))      
        print('\nThe following is a display of the new product ID {} data :'.format(id))
        headerTable()
        print('|',id,'   |',productName,' '*(31-len(productName)),'|',productCategory,'\t|',productStock,'\t|',productPrice,'| ')
        print('-'*82)
        saveDecision = input('\nDo you want to add the new product ID {} above (YES/NO) ? '.format(id))       
        if (saveDecision.lower() == 'yes') :
            productData[id] = {'name': productName,'category': productCategory,'stock': productStock,'price': productPrice}
            allDataTable()
            print('\nThe new product ID {} has been successfully added and saved!'.format(id))          
            addMenu()
        elif (saveDecision.lower() == 'no') :
            allDataTable()
            print('\nThe new product ID {} not being added!'.format(id))
            addMenu()
        else :
            print('\nYour input is invalid! Recognized input value : YES or NO !')
            addMenu()

def updateMenu() :
    updateMenuOption = input('''
        Welcome to UPDATE Product Data Menu!
         
        Menu Options :
        1. Update Existing Product Data
        2. Go Back to Main Menu
            
        Please input the number of option you want to run (1/2) : ''')    
    if (updateMenuOption == '1') :
        updateExistingData()
    elif (updateMenuOption == '2') :
        mainMenu()
    else :
        print('\nYour input is invalid! Recognized input value : 1 or 2 !')
        updateMenu()

def updateExistingData() :
    id = input('\nPlease input the Product ID to be updated : ')
    if id in productData.keys() :
        specificDataTable(id)
        updateContinue = input('\nDo you want to update the product ID {} above (YES/NO) ? '.format(id))  
        if (updateContinue.lower() == 'no') :
            noUpdate(id)
        elif (updateContinue.lower() == 'yes') :
            column = (input('''
            List of Column :
            > Product ID
            > Product Name
            > Product Cetegory
            > Product Stock
            > Product Price
            
            Which column to be updated (id/name/category/stock/price) ? '''))
            if (column.lower() == 'id') :
                newValue = input('\nPlease input the new product ID value : ')
                print('\nThe following is a display of updated product ID from product ID {} data :'.format(id))
                headerTable()
                print('|',newValue,'   |',productData[id]['name'],' '*(31-len(productData[id]['name'])),'|',productData[id]['category'],'\t|',productData[id]['stock'],'\t|',productData[id]['price'],'| ')
                print('-'*82)
                decisionUpdate(id, column, newValue)
            elif (column.lower() == 'name') :
                newValue = input('\nPlease input the new product name value : ')
                print('\nThe following is a display of updated name from product ID {} data :'.format(id))
                headerTable()
                print('|',id,'   |',newValue,' '*(31-len(newValue)),'|',productData[id]['category'],'\t|',productData[id]['stock'],'\t|',productData[id]['price'],'| ')
                print('-'*82)
                decisionUpdate(id, column, newValue)
            elif (column.lower() == 'category') :
                newValue = input('\nPlease input the new product category value : ')
                print('\nThe following is a display of updated category from product ID {} data :'.format(id))
                headerTable()
                print('|',id,'   |',productData[id]['name'],' '*(31-len(productData[id]['name'])),'|',newValue,'\t|',productData[id]['stock'],'\t|',productData[id]['price'],'| ')
                print('-'*82)
                decisionUpdate(id, column, newValue)
            elif (column.lower() == 'stock') :
                newValue = int(input('\nPlease input the new product stock value : '))
                print('\nThe following is a display of updated stock from product ID {} data :'.format(id))
                headerTable()
                print('|',id,'   |',productData[id]['name'],' '*(31-len(productData[id]['name'])),'|',productData[id]['category'],'\t|',newValue,'\t|',productData[id]['price'],'| ')
                print('-'*82)
                decisionUpdate(id, column, newValue)
            elif (column.lower() == 'price') :
                newValue = int(input('\nPlease input the new product price value : '))
                print('\nThe following is a display of updated price from product ID {} data :'.format(id))
                headerTable()
                print('|',id,'   |',productData[id]['name'],' '*(31-len(productData[id]['name'])),'|',productData[id]['category'],'\t|',productData[id]['stock'],'\t|',newValue,'| ')
                print('-'*82)
                decisionUpdate(id, column, newValue)
            else :
                print('\nYour input is invalid!\nRecognized input value : "id" or "name" or "category" or "stock" or "price" !')
                updateMenu()
        else :
            invalidUpdate()
    else :
        idNotFound(id)
        updateMenu()

def noUpdate(id) :
    allDataTable()
    print('\nThe existing product ID {} not being updated!'.format(id))
    updateMenu()

def decisionUpdate(id, column, newValue) :
    updateDecision = input('\nAre you sure want to update the product ID {} above (YES/NO) ? '.format(id))
    if (updateDecision.lower() == 'yes') :
        if (column.lower() == 'id') :
            valueID = productData.pop(id)
            productData[newValue] = valueID
            successUpdate(id)
        elif (column.lower() == 'name' or column.lower() == 'category' or column.lower() == 'stock' or column.lower() == 'price') :
            productData[id][column] = newValue
            successUpdate(id)
    elif (updateDecision.lower() == 'no') :
        noUpdate(id)
    else :
        invalidUpdate()

def successUpdate(id) :
    allDataTable()
    print('\nThe product ID {} has been successfully updated!'.format(id))
    updateMenu()

def invalidUpdate() :
    print('\nYour input is invalid! Recognized input value : YES or NO !')
    updateMenu()

def deleteMenu() :
    deleteMenuOption = input('''
        Welcome to DELETE Product Data Menu!
         
        Menu Options :
        1. Delete Existing Product Data
        2. Go Back to Main Menu
            
        Please input the number of option you want to run (1/2) : ''')    
    if (deleteMenuOption == '1') :
        deleteExistingData()
    elif (deleteMenuOption == '2') :
        mainMenu()
    else :
        print('\nYour input is invalid! Recognized input value : 1 or 2 !')
        deleteMenu()

def deleteExistingData() :
    id = input('\nPlease input the Product ID to be deleted : ')
    if id in productData.keys() :
        specificDataTable(id)
        deleteDecision = input('\nAre you sure want to delete the product ID {} above (YES/NO) ? '.format(id))
        if (deleteDecision.lower() == 'yes') :
            del productData[id]
            allDataTable()
            print('\nThe product ID {} has been successfully deleted!'.format(id))
            deleteMenu()
        elif (deleteDecision.lower() == 'no') :
            allDataTable()
            print('\nThe product ID {} not being deleted!'.format(id))
            deleteMenu()
        else :
            print('\nYour input is invalid! Recognized input value : YES or NO !')
            deleteMenu()
    else :
        idNotFound(id)
        deleteMenu()

mainMenu()

