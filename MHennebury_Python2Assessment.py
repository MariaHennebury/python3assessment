#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Ask the user to enter the first integer
first_number = int(input("Enter the first integer: "))

# Ask the user to enter the second integer
second_number = int(input("Enter the second integer: "))

# Ask the user to enter the third integer
third_number = int(input("Enter the third integer: "))

# Make the data into a list
intergers = list((first_number, second_number, third_number))
print('intergers are:', intergers)

# Calculate the sum of the three integers
sum_result = sum(intergers)
print("The sum is:", sum_result)

# Calculate the average of the three integers
avg_result = int(sum_result / 3)
print("The average is:", avg_result)

# Calculate Min + max
print("The Min is:", min(intergers))
print("The Max is:", max(intergers))

# Append List and recalculatee
intergers.append(avg_result)
print('intergers are now:', intergers)
new_sum = int(sum(intergers))
print("The sum is now:", new_sum)
updated_average = int(new_sum / 4)
print('Updated average is:', updated_average)
print("The Updated Min is:", min (intergers))
print("The Updated Max is:", max (intergers))

# Ask the user to enter the fifth integer
fifth_number = int(input("Enter the next integer: "))

# Append List
intergers.append(fifth_number)

# Sort descending order
results = sorted(intergers, reverse=True)
print ('the intergers are now:', results)


# In[ ]:




