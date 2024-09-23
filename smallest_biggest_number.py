#give biggest and smallest number in the input of 5 numbers

#put in github


while True:
    
    empty_list=[]
    
    
    list_of_numbers=input('Write 5 numbers to find largest and smallest one or press enter to exit: ')
    
    if list_of_numbers=='':
        break
        
    list_of_numbers=list_of_numbers.split()

    
    
    if len(list_of_numbers) !=5:
        print('Your numbers were not 5')
        break
        

    elif len(list_of_numbers)==5:
        
        for numbers in list_of_numbers:
            numbers=int(numbers)
            empty_list.append(numbers)
            
        #print(empty_list)
                        
        min_number=min(empty_list)
        max_number=max(empty_list)
            
    
    

    print('Minimum number is: ', min_number)
    print('Maximum number is: ', max_number)
    
    


#another way of doing it

# while True:
    
#     empty_list=[]
    
    
#     list_of_numbers=input('Enter 5 numbers or press enter to exit: ')
    
#     if list_of_numbers=='':
#         break
        
#     list_of_numbers=list_of_numbers.split()
    
    
#     if len(list_of_numbers) !=5:
#         print('Your numbers were not 5')
#         break
        

#     elif len(list_of_numbers)==5:
        
#         for numbers in range(len(list_of_numbers)): 
#             empty_list.append(int(list_of_numbers[numbers]))
        
#         print(empty_list)
        
#         min_number=min(empty_list)
#         max_number=max(empty_list)
            
    
    

#     print('minimum number is: ', min_number)
#     print('maximum number is: ', max_number)