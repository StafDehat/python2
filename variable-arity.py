def fn1(*args):
  print type(args), args, isinstance(args[1],str), isinstance(args[1],int)

fn1(2,3,4)

lst=[1,2,3]
fn1(*lst)
