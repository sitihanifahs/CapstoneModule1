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
    print('-'*83)
    print('| Product ID | Product Name\t\t\t| Category\t| Stock\t| Price   |')
    print('-'*83)

def allDataTable() :
    print('\nThe following is a display of all existing data products :')
    headerTable()
    for id in productData :
        print('|',id,'   |',productData[id]['name'],' '*(31-len(productData[id]['name'])),'|',productData[id]['category'],' '*(12-len(productData[id]['category'])),'|',productData[id]['stock'],' '*(4-len(str(productData[id]['stock']))),'|',productData[id]['price'],' '*(6-len(str(productData[id]['price']))),'|')
    print('-'*83)

def noDataNotif() :
    print("\nThere aren't available data to display!")
    readMenu()

def displaySpecificData() :
    if (len(productData)>0) :
        id = input('\nPlease input the specific Product ID to be displayed : ').upper()
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
    print('|',id,'   |',productData[id]['name'],' '*(31-len(productData[id]['name'])),'|',productData[id]['category'],' '*(12-len(productData[id]['category'])),'|',productData[id]['stock'],' '*(4-len(str(productData[id]['stock']))),'|',productData[id]['price'],' '*(6-len(str(productData[id]['price']))),'|')
    print('-'*83)

def idNotFound(id) :
    allDataTable()
    print('\nThe product ID {} not found!'.format(id))  

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
    id = input('\nPlease input the new Product ID : ').upper()
    if id in productData.keys() :
        specificDataTable(id)
        print("\nThe Product ID {} already exists! You can't add a duplicate Product ID!".format(id))
        addMenu()
    else :
        if (len(id) == 7) :
            productName = input('Please input the product name : ').title()
            if (len(productName) > 31) :
                productName = productName[:31]
            productCategory = input('Please input the product category : ').title()
            if (len(productCategory) > 12) :
                productCategory = productCategory[:12]
            while True :
                try :
                    productStock = int(input('Please input the product stock : '))
                    break
                except ValueError :
                    print("\nYou can't input non integer value for Product Stock!\nPlease input an integer value for Product Stock!\n")
            if (len(str(productStock)) > 4) :
                productStock = int(str(productStock)[:4])
            while True :
                try :
                    productPrice = int(input('Please input the product price : '))
                    break
                except ValueError :
                    print("\nYou can't input non integer value for Product Price!\nPlease input an integer value for Product Price!\n") 
            if (len(str(productPrice)) > 6) :
                productPrice = int(str(productPrice)[:6])
            print('\nThe following is a display of the new product ID {} data :'.format(id))
            headerTable()
            print('|',id,'   |',productName,' '*(31-len(productName)),'|',productCategory,' '*(12-len(productCategory)),'|',productStock,' '*(4-len(str(productStock))),'|',productPrice,' '*(6-len(str((productPrice)))),'|')
            print('-'*83)
            saveDecision = input('\nDo you want to add the new product ID {} above (YES/NO) ? '.format(id)).lower()       
            if (saveDecision == 'yes') :
                productData[id] = {'name': productName,'category': productCategory,'stock': productStock,'price': productPrice}
                allDataTable()
                print('\nThe new product ID {} has been successfully added and saved!'.format(id))          
                addMenu()
            elif (saveDecision == 'no') :
                allDataTable()
                print('\nThe new product ID {} not being added!'.format(id))
                addMenu()
            else :
                print('\nYour input is invalid! Recognized input value : YES or NO !')
                addMenu()
        else :
            print('\nThe new Product ID {} is invalid! Recognized input value is 7 characters!'.format(id))
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
    id = input('\nPlease input the Product ID to be updated : ').upper()
    if id in productData.keys() :
        specificDataTable(id)
        updateContinue = input('\nDo you want to update the product ID {} above (YES/NO) ? '.format(id)).lower()  
        if (updateContinue == 'no') :
            noUpdate(id)
        elif (updateContinue == 'yes') :
            column = input('''
            List of Column :
            > Product ID
            > Product Name
            > Product Cetegory
            > Product Stock
            > Product Price
            
            Which column to be updated (id/name/category/stock/price) ? ''').lower()
            if (column == 'id') :
                newValue = input('\nPlease input the new product ID value : ').upper()
                if (len(newValue) == 7) :
                    print('\nThe following is a display of updated product ID from product ID {} data :'.format(id))
                    headerTable()
                    print('|',newValue,'   |',productData[id]['name'],' '*(31-len(productData[id]['name'])),'|',productData[id]['category'],' '*(12-len(productData[id]['category'])),'|',productData[id]['stock'],' '*(4-len(str(productData[id]['stock']))),'|',productData[id]['price'],' '*(6-len(str(productData[id]['price']))),'|')
                    print('-'*83)
                    decisionUpdate(id, column, newValue)
                else :
                    print('\nThe new Product ID {} is invalid! Recognized input value is 7 characters!'.format(id))
                    updateExistingData()
            elif (column == 'name') :
                newValue = input('\nPlease input the new product name value : ').title()
                if (len(newValue) > 31) :
                    newValue = newValue[:31]
                print('\nThe following is a display of updated name from product ID {} data :'.format(id))
                headerTable()              
                print('|',id,'   |',newValue,' '*(31-len(newValue)),'|',productData[id]['category'],' '*(12-len(productData[id]['category'])),'|',productData[id]['stock'],' '*(4-len(str(productData[id]['stock']))),'|',productData[id]['price'],' '*(6-len(str(productData[id]['price']))),'|')
                print('-'*83)
                decisionUpdate(id, column, newValue)
            elif (column == 'category') :
                newValue = input('\nPlease input the new product category value : ').title()
                if (len(newValue) > 12) :
                    newValue = newValue[:12]
                print('\nThe following is a display of updated category from product ID {} data :'.format(id))
                headerTable()
                print('|',id,'   |',productData[id]['name'],' '*(31-len(productData[id]['name'])),'|',newValue,' '*(12-len(newValue)),'|',productData[id]['stock'],' '*(4-len(str(productData[id]['stock']))),'|',productData[id]['price'],' '*(6-len(str(productData[id]['price']))),'|')
                print('-'*83)
                decisionUpdate(id, column, newValue)
            elif (column == 'stock') :
                while True :
                    try :
                        newValue = int(input('\nPlease input the new product stock value : '))
                        break
                    except ValueError :
                        print("\nYou can't input non integer value for Product Stock!\nPlease input an integer value for Product Stock!")
                if (len(str(newValue)) > 4) :
                    newValue = int(str(newValue)[:4])
                print('\nThe following is a display of updated stock from product ID {} data :'.format(id))
                headerTable()
                print('|',id,'   |',productData[id]['name'],' '*(31-len(productData[id]['name'])),'|',productData[id]['category'],' '*(12-len(productData[id]['category'])),'|',newValue,' '*(4-len(str(newValue))),'|',productData[id]['price'],' '*(6-len(str(productData[id]['price']))),'|')
                print('-'*83)
                decisionUpdate(id, column, newValue)
            elif (column == 'price') :
                while True :
                    try :
                        newValue = int(input('\nPlease input the new product price value : '))
                        break
                    except ValueError :
                        print("\nYou can't input non integer value for Product Price!\nPlease input an integer value for Product Price!")
                if (len(str(newValue)) > 6) :
                    newValue = int(str(newValue)[:6])
                print('\nThe following is a display of updated price from product ID {} data :'.format(id))
                headerTable()
                print('|',id,'   |',productData[id]['name'],' '*(31-len(productData[id]['name'])),'|',productData[id]['category'],' '*(12-len(productData[id]['category'])),'|',productData[id]['stock'],' '*(4-len(str(productData[id]['stock']))),'|',newValue,' '*(6-len(str(newValue))),'|')
                print('-'*83)
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
    updateDecision = input('\nAre you sure want to update the product ID {} above (YES/NO) ? '.format(id)).lower()
    if (updateDecision == 'yes') :
        if (column == 'id') :
            if newValue in productData.keys() :
                allDataTable()
                print("\nYou can't update Product ID {} to the new value {}!\nThis because Product ID {} already exist as shown above!\nPlease use other new Product ID value!".format(id,newValue,newValue))
                updateMenu()
            else :
                valueID = productData.pop(id)
                productData[newValue] = valueID
                successUpdate(id)
        elif (column == 'name' or column == 'category' or column == 'stock' or column == 'price') :
            productData[id][column] = newValue
            successUpdate(id)
    elif (updateDecision == 'no') :
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
    id = input('\nPlease input the Product ID to be deleted : ').upper()
    if id in productData.keys() :
        specificDataTable(id)
        deleteDecision = input('\nAre you sure want to delete the product ID {} above (YES/NO) ? '.format(id)).lower()
        if (deleteDecision == 'yes') :
            del productData[id]
            allDataTable()
            print('\nThe product ID {} has been successfully deleted!'.format(id))
            deleteMenu()
        elif (deleteDecision == 'no') :
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

