# for slicing collection must is in form of ordered collection
#   ex.==>(string,list,tuple)
# syntax ==> collection[startpoint:stop:step/jump/direction]
# rule==> 1. check direction of the step
#    if step/jump/direction is empty(collection [startpoint:endpoint]) than by default
#    its 1.
#     +ve step (+ve diection)
#     -ve step (-ve diection)

#     2.check start-stop direction
#     3. if both dirction are matching then we get output otherwise
#     it gives empty output
str1='python'
print(str1[::-1])  #(output reverse of the string direction -ve)
print(str1[::])  # output print the string direction +ve