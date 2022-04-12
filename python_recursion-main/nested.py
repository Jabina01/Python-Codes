# import types

# def nested_to_flat(lis):
#     flat_list = []
#     index = 0

#     while (index < len(lis)):

#         element = lis[index]

#         if type(element) != types.IntType:
#             flat_list = flat_list + nested_to_flat(element)
#         else:
#             flat_list.append(element)

#         index += 1

#     return flat_list
# print(nested_to_flat([1,4][2,[1]]))




def recursion_sum(my_list):
   my_total = 0
   for elem in my_list:
      if (type(elem) == type([])):
         my_total = my_total + recursion_sum(elem)
      else:
         my_total = my_total + elem
   return my_total
my_list = [1,2,[3,4],[5,6]]
print(recursion_sum(my_list))
