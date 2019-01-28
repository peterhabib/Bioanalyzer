# # in_file = "/home/peter/Desktop/Moduls/test_data/result.txt"
# # open_file = open(in_file , 'r')
# # read_file = open_file.readlines()
# # strlen = len(read_file)
# # print(strlen)
# #
# # list = []
# # for lines in read_file:
# #     list.append(lines.strip())
# #
# # print(list)
# # print("")
# #
# # list2 = []
# # endproccess = 0
# # for i in range(10):
# #     while endproccess < strlen:
# #         start = 0
# #         end = 2
# #         list2.append(list[0][start:end])
# #         list2.append(list[1][start:end])
# #         list2.append(list[2][start:end])
# #         start += 1
# #         end += 1
# #         endproccess +=  1
# #
# #
# # print(list2)
#
#
#
#
# string = ['AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA','CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC','VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV']
# lens = len(string[0])
# print(lens)
# #print(string[0:10])
#
#
#
#
# def slicing():
#     try:
#         list2 = []
#
#         endproc = 0
#         pos = 0
#         start = 0
#         end = 5
#         ind = 0
#         while endproc < lens:
#             list2.insert(ind , string[pos][start:end])
#             end = end + 5
#             start = start + 5
#             endproc = endproc + 1
#             if endproc == lens:
#                 del string[0]
#                 ind = ind + 5
#                 slicing()
#     except IndexError:
#         return
#     print(list2)
# slicing()
#
#
# print(string)



