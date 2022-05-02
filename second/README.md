### Problem Statement 
Describe a stepwise methodology using pseudocode/specific code to auto generate a list of products/items with low stock/expiry from the inventory database. The list must be updated at 12 A.M. daily.


### Answer:
**Stock Model:**
   - Lead time:- time lag from the date of placing an order for material and the date on which materials are received.
    
    - Safety Stock:- minimum level of inventory that is held as a protection against shortages

    - current stock :- currently available stock in inventory

    - Maximum stock:- Maximu available stock

    - Expiry Data

#### Expiry - 

Consider constant time of 1 week.
We have to check for the items daily at 12 A.M.

Pseudocode:
```
if item has expired,
    then restock the items
```

#### Low Stock
- we use th concept of reorder point, which is minimum amount of an item which a firm holds in stock, such that, when stock falls to this amount, the item must be reordered.
- To calculate reorder level, we need to caculate average daily usage, lead time

Reorder Level = Avarage Daily Usage * Lead time in days

``` 
if current stock  < reorder level:
    then restock
```

### Task Scheduling
To perform above activities daily at 12 A.M we can use celery module of python to schedule inventory stock check.

``` Pseudocode:
from celery.schedules import crontab
from celery.decorators import periodic_task

@periodic_task(run_every = crontab(minute=0, hour=0))
# task to be performed like restocking, inventory check etc

```




