### Problem Statement

1. Develop an application that generates invoices in fairly simple format. Format  for reference can be found at the end of this task. You can make a model for  items and other details as per your convenience. The application must facilitate  the following API(s): 
a. GET: get the list of available items with details such as (name, price,  description). 
b. POST: to send the list of items to buy with corresponding quantities. c. PUT: to update the list of items in the purchase list. 
d. GET: get the invoice for the purchase in pdf format as per the above  format but with all the necessary details filled dynamically. 
Configure and deploy the application mentioned in first point to any open and  free hosting service like Heroku/PythonAnywhere. Add the link to the project. 


#### Models Used
1. Items
    - Contains info about items such as item_name, description, price
    - ![image](https://user-images.githubusercontent.com/60350731/166231152-ae21811e-3c06-47dd-a636-9b754020f093.png)

		
2. Invoice 
    - Contains item quantity purchased, and item description
    - ![image](https://user-images.githubusercontent.com/60350731/166231202-b0de67d9-2947-477e-bc21-028cd38f30e6.png)


#### API Endpoints

 1. /items - 
			
      - **GET method**:
				Returns a list of all the available items in the database in json format.
        ![image](https://user-images.githubusercontent.com/60350731/166231008-6d76363a-fd62-458e-98ba-07cfddcd5d8d.png)

        
      - **POST method:**
      - This method is used to add new items to the list.
      ![image](https://user-images.githubusercontent.com/60350731/166231391-2a152b1c-919c-4c81-bacf-63f526d4eb44.png)
       
      - New item added is showm like this
      ![image](https://user-images.githubusercontent.com/60350731/166231542-342cf9c8-35a9-48ad-8610-34fed49a97ea.png)

 
2. /invoice - 
      
      - **GET method:**
        Returns a list of all the invoices. 
        ![image](https://user-images.githubusercontent.com/60350731/166231819-3b3677b6-ec64-46db-bf3c-12702ecb0f40.png)
      
      
      - **POST method:**
		     To post list of items to buy with corresponding quantities.
         ![image](https://user-images.githubusercontent.com/60350731/166232143-c458858c-9ab2-4292-8c2a-c934b9e70346.png)
        
        New item added with quantity
		    ![image](https://user-images.githubusercontent.com/60350731/166232214-b5fe91c9-abe9-4b8f-afe0-7bbf3d618964.png)

        
      - **PUT method:**
      - TO update quantity of the item
      ![image](https://user-images.githubusercontent.com/60350731/166232411-fd488ca8-7cbb-4dd3-aa6f-50680b14034b.png)
      
      - After updating quantity
      ![image](https://user-images.githubusercontent.com/60350731/166232562-97a2bfa6-12e0-4a5e-b8b9-960869eaa073.png)


		  
3. /generate_invoice
	- Generates a pdf and returns a pdf which can be downloaded.
	- ![image](https://user-images.githubusercontent.com/60350731/166232680-bf097d42-7648-4cf8-8e93-31cfe35972ee.png)	


### Deployment: 
- App is deployed on heroku
- API Root Link:  https://invoice-drf.herokuapp.com/
- Items Link: https://invoice-drf.herokuapp.com/items/
- Invoices Link: https://invoice-drf.herokuapp.com/invoice/
- Generate_Invoice Link: https://invoice-drf.herokuapp.com/generate_invoice/
