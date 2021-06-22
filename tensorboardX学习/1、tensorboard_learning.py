from tensorboardX import SummaryWriter

# Creates writer1 object.
# The log will be saved in 'runs/exp'
#writer1 = SummaryWriter('runs/exp')

# # Creates writer2 object with auto generated file name
# # The log directory will be something like 'runs/Aug20-17-20-33'
# writer2 = SummaryWriter()
#
# # Creates writer3 object with auto generated file name, the comment will be appended to the filename.
# # The log directory will be something like 'runs/Aug20-17-20-33-resnet'
# writer3 = SummaryWriter(comment='resnet')

from tensorboardX import SummaryWriter

writer = SummaryWriter('runs/scalar_example')
for i in range(10):
    '''
    第一个参数可以简单理解为保存图的名称，第二个参数是可以理解为Y轴数据，第三个参数可以理解为X轴数据
    '''
    writer.add_scalar('quadratic', i**2, global_step=i)
    writer.add_scalar('exponential', 2**i, global_step=i)

writer.close()