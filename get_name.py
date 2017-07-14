>>> names = ["Alex","Tenglan","Eric","Rain","Tom","Amy"]
>>> names[1:4]  #取下标1至下标4之间的数字，包括1，不包括4
['Tenglan', 'Eric', 'Rain']
>>> names[1:-1] #取下标1至-1的值，不包括-1
['Tenglan', 'Eric', 'Rain', 'Tom']
>>> names[0:3] 
['Alex', 'Tenglan', 'Eric']
>>> names[:3] #如果是从头开始取，0可以忽略，跟上句效果一样
['Alex', 'Tenglan', 'Eric']
>>> names[3:] #如果想取最后一个，必须不能写-1，只能这么写
['Rain', 'Tom', 'Amy'] 
>>> names[3:-1] #这样-1就不会被包含了
['Rain', 'Tom']
>>> names[0::2] #后面的2是代表，每隔一个元素，就取一个
['Alex', 'Eric', 'Tom'] 
>>> names[::2] #和上句效果一样
['Alex', 'Eric', 'Tom']
