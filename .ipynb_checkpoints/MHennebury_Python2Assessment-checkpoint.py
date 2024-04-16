#!/usr/bin/env python
# coding: utf-8

# In[43]:


# Ask the user to enter the first integer
first_number = int(input("Enter the first integer: "))

# Ask the user to enter the second integer
second_number = int(input("Enter the second integer: "))

# Ask the user to enter the third integer
third_number = int(input("Enter the third integer: "))

# Make a list
intergers = list((first_number, second_number, third_number))
print('intergers:', intergers)

# Calculate the sum of the three integers
sum_result = sum(intergers)
print("The sum is:", sum_result)

# Calculate the average of the three integers
avg_result = sum_result / 3

# Print the avg
print("The average is:", avg_result)

# Calculate Min + max
print("The Min is:", min(intergers))
print("The Max is:", max(intergers))

# Append List
intergers.append(avg_result)
print('intergers are now:', intergers)

# print new sum
new_sum = sum(intergers)
print ('the new sum is:', new_sum)

# Print new avg
new_avg = (new_sum / 4)
print('new average is:', new_avg)

# Calculate Min + max
print("The Min is:", min (intergers))
print("The Max is:", max (intergers))

# Ask the user to enter the fifth integer
fifth_number = int(input("Enter the next integer: "))

# Append List
intergers.append(fifth_number)

# Sort descending order
results = sorted(intergers, reverse=True)
print ('the intergers are now:', results)


# In[ ]:




