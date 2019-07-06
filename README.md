# Add cities to their id

## Introduction  
This work is designed to parse the Arabic texts files and add to each **city name** in the **files processed** by its id provided that they are listed in the **coordinates file**

### The problems we encountered
* Nature of Arabic Language
* Names of cities containing the name of another city
> Example

#### The coordinates file contains

| Country| City | X coordinates |y coordinates|id |
| ------- | :------------ |------------: | :------------ |------------: |
| اليمن| إب| 13.979|45.574| coord1            |
| اسبانيا| إبار| 32.7604|21.62| coord2            |
 
#### Implementation 

##### إبار
>ار coord1 اب

### The solution
Take the name of the mandate and withdraw the names of states overlapping with the selected mandate and implementation

> Example

#### The coordinates file contains

| Country| City | X coordinates |y coordinates|id |
| ------- | :------------ |------------: | :------------ |------------: |
| اليمن| إب| 13.979|45.574| coord1            |
| اسبانيا| إبار| 32.7604|21.62| coord2            |
 
#### Implementation 

1. **Extracting city information** [["إب","coord1"]]
2. **Search for similarities** [["إب","coord1"],* ["إبار","coord2"]]
3. **the change coord2** إبار

## Technologies
 Sort the binaries to families by the root of the word and start changing the text on the large root until we get to the name we started with. Repeat this process with each line of text
## Explain how to work
 1.  Read the coordinate file and take the required diodes **[name_city,id]**
> Example
~~~
[
     ['Namecity1', ' coord1']    ,
     ['Namecity2', ' coord2']    ,
             ...,
     ['Namecityn', ' coordn']
]
~~~

 2.  Categorize information extracted based on the similarity of state names

> Example
~~~
[
    [['Namecity1', ' coord0'],...]
        # If the city name is single 
    [['Namecity2', ' coord1 coord2 '],...]  
        # If the same city name and id are different 
    [[' Namecity3 ', ' coord3'] ,[' Namecity4 ', ' coord4'],...]  
        # If the name of the city contained in the second 
    [[' Namecity5 ', ' coord5'] ,[' Namecity6 ', ' coord6 coord7'],...] 
        # All previous situations together 
]
~~~
3.  Reads a line from the corpus file
4. Pass the list and change all the names of the cities in the list and the line read [id]
> **Note:** The name of the city is replaced with [id] to avoid error while returning city names 
**(coord1021 and coord10 => name_city21)**
5. Repeat the process with all the extracted diodes and record all the diodes used
6. From the second list used, replace the read line with each [id] with name_city id
7. Record the readable line after the updates in a file that has the same path and file name as the original by adding one number in the file name of the originator namefile1
> **Note:** We took this action for
>* Avoid reading the entire file and changing the file size not to ensure
>* When you finish the changes in each line of the file, delete the original file and delete the one added in the originator file

## Example of implementation
### input
---
1. File coordinates

| Country| City | X coordinates |y coordinates|id |
| ------- | :------------ |------------: | :------------ |------------: |
| اليمن| إب| 13.979|45.574| coord1            |
| اسبانيا| إبار| 32.7604|21.62| coord2            |
| اليمن| البيضاء| 12.02|55.2| coord3            |
| ليبيا| البيضاء| 10.32|25.36| coord4           |
| المغرب| الدار البيضاء| 12.32|100.2| coord5            |

2. File corpus
~~~
مدينة إبار الاسبانية منتجع كبير لسايح
البيضاء من اكبر المدن تعداد لسكان على غرار الدار البيضاء
~~~
---
### Implementation
---
1.   Read the coordinate file and take the required diodes
~~~
[
     ['إب', ' coord1']    ,
     ['إبار', ' coord2']    ,
     ['البيضاء', ' coord3']    ,
     ['البيضاء', ' coord4']    ,
     ['الدار البيضاء', ' coord5']    
]
~~~
2. Categorize information extracted based on the similarity of state names
~~~
[
     [['إب', ' coord1'],['إبار', ' coord2']],
     [['البيضاء', ' coord3 coord4'],['الدار البيضاء', ' coord5']]    
]
~~~
3.  Reads a line from the corpus file
>3.1. line 1 : مدينة إبار الاسبانية منتجع كبير لسايح
~~~
3.1.1. # the change
* [['إب', ' coord1'],['إبار', ' coord2']]
   * ['إبار', ' coord2'] => الاسبانية منتجع كبير لسايح [coord2]  مدينة  Change List =[['إبار', ' coord2']]
   * ['إب', ' coord1'] => الاسبانية منتجع كبير لسايح [coord2]  مدينة Change List =[['إبار', ' coord2']]
* [['البيضاء', ' coord3 coord4'],['الدار البيضاء', ' coord5']]    
   * ['الدار البيضاء', ' coord5'] => الاسبانية منتجع كبير لسايح [coord2]  مدينة Change List =[['إبار', ' coord2']]
   * ['البيضاء', ' coord3 coord4'] => الاسبانية منتجع كبير لسايح [coord2]  مدينة Change List =[['إبار', ' coord2']]
~~~
~~~
3.1.2. # Retrieve city name
* Change List =[['إبار', ' coord2']] => الاسبانية منتجع كبير لسايح coord2 مدينة إبار
* Change List =[] => الاسبانية منتجع كبير لسايح coord2 مدينة إبار
~~~
~~~
3.1.3. # Write in the new file
الاسبانية منتجع كبير لسايح coord2 مدينة إبار
~~~
> 3.2 line 2: البيضاء من اكبر المدن تعداد لسكان على غرار الدار البيضاء

~~~
3.1.1. # the change
* [['إب', ' coord1'],['إبار', ' coord2']]
   * ['إبار', ' coord2'] =>البيضاء من اكبر المدن تعداد لسكان على غرار الدار البيضاء
  Change List =[]
   * ['إب', ' coord1'] => البيضاء من اكبر المدن تعداد لسكان على غرار الدار البيضاء
 Change List =[]
* [['البيضاء', ' coord3 coord4'],['الدار البيضاء', ' coord5']]    
   * ['الدار البيضاء', ' coord5'] =>[coord5] البيضاء من اكبر المدن تعداد لسكان على غرار 
Change List =[['الدار البيضاء', ' coord5']]
   * ['البيضاء', ' coord3 coord4'] => 
 [coord5] من اكبر المدن تعداد لسكان على غرار [coord3 coord4] 
Change List =[['الدار البيضاء', ' coord5'],['البيضاء', ' coord3 coord4']]
~~~
~~~
3.1.2. # Retrieve city name
* Change List =[['الدار البيضاء', ' coord5'],['البيضاء', ' coord3 coord4']]
                     => [coord5] من اكبر المدن تعداد لسكان على غرار coord3 coord4 البيضاء
* Change List =[['البيضاء', ' coord3 coord4']] 
                     => coord5 تعد من اكبر المدن تعدادا لسكان على غرار الدار البيضاء coord3 coord4 البيضاء 
* Change List =[] 
                     =>  coord5 تعد من اكبر المدن تعدادا لسكان على غرار الدار البيضاء coord3 coord4 البيضاء
~~~
~~~
3.1.3. # Write in the new file
الاسبانية منتجع كبير لسايح coord2 مدينة إبار
 coord5 تعد من اكبر المدن تعدادا لسكان على غرار الدار البيضاء coord3 coord4 البيضاء
~~~
---
> END Example 



